# Databricks Notebook 6: Gold Layer — Monthly Customer Churn by City
# ================================================================
# Builds swiggy.gold.monthly_customer_churn from silver orders and customers.

# COMMAND ----------
SILVER_ORDERS = "swiggy.silver.orders_clean"
SILVER_CUSTOMERS = "swiggy.silver.customers"
GOLD_MONTHLY_CUSTOMER_CHURN = "swiggy.gold.monthly_customer_churn"

# COMMAND ----------
from pyspark.sql.functions import (
    add_months,
    coalesce,
    col,
    countDistinct,
    current_timestamp,
    date_trunc,
    lit,
    max as spark_max,
    round,
    when,
)

# COMMAND ----------
# %md
# ## 6.1 Load silver orders and customers

# COMMAND ----------
orders = (
    spark.table(SILVER_ORDERS)
    .filter(col("is_valid_order") == True)
    .filter(col("customer_id").isNotNull())
    .filter(col("placed_at").isNotNull())
)

customers = (
    spark.table(SILVER_CUSTOMERS)
    .filter(col("is_current") == True)
    .select("customer_id", "customer_city")
)

# COMMAND ----------
# %md
# ## 6.2 Monthly customer activity by city
# A customer is active in month M if they placed at least one valid order in that city during M.

# COMMAND ----------
customer_monthly_activity = (
    orders.alias("o")
    .join(customers.alias("c"), "customer_id", "left")
    .withColumn("order_month", date_trunc("month", col("placed_at")))
    .withColumn("city", coalesce(col("o.city"), col("c.customer_city")))
    .filter(col("city").isNotNull())
    .select("customer_id", "city", "order_month")
    .distinct()
)

active_by_month = (
    customer_monthly_activity
    .groupBy("city", "order_month")
    .agg(countDistinct("customer_id").alias("active_customers"))
)

# COMMAND ----------
# %md
# ## 6.3 Identify churned customers
# A customer churns in city C for month M if they ordered in C during M but not during M+1.

# COMMAND ----------
activity_with_next_month = customer_monthly_activity.withColumn(
    "next_month", add_months(col("order_month"), 1)
)

next_month_activity = customer_monthly_activity.select(
    col("customer_id").alias("next_customer_id"),
    col("city").alias("next_city"),
    col("order_month").alias("next_order_month"),
)

churned_customers = (
    activity_with_next_month.alias("curr")
    .join(
        next_month_activity,
        (col("curr.customer_id") == col("next_customer_id"))
        & (col("curr.city") == col("next_city"))
        & (col("curr.next_month") == col("next_order_month")),
        "left_anti",
    )
    .select(
        col("curr.city"),
        col("curr.order_month").alias("activity_month"),
        col("curr.customer_id"),
    )
)

churned_by_month = (
    churned_customers
    .groupBy("city", "activity_month")
    .agg(countDistinct("customer_id").alias("churned_customers"))
)

# COMMAND ----------
# %md
# ## 6.4 Calculate monthly churn rate by city
# churn_rate = churned_customers / active_customers

# COMMAND ----------
max_activity_month = customer_monthly_activity.agg(
    spark_max("order_month").alias("max_month")
)

monthly_customer_churn = (
    active_by_month.alias("active")
    .join(
        churned_by_month.alias("churned"),
        (col("active.city") == col("churned.city"))
        & (col("active.order_month") == col("churned.activity_month")),
        "left",
    )
    .select(
        col("active.city"),
        col("active.order_month").alias("month"),
        col("active.active_customers"),
        coalesce(col("churned.churned_customers"), lit(0)).alias("churned_customers"),
    )
    .withColumn(
        "churn_rate",
        when(
            col("active_customers") > 0,
            round(col("churned_customers") / col("active_customers"), 4),
        ).otherwise(lit(0.0)),
    )
    .withColumn("gold_processed_at", current_timestamp())
    .join(max_activity_month)
    .filter(col("month") < col("max_month"))
    .drop("max_month")
)

# COMMAND ----------
# %md
# ## 6.5 Write gold table

# COMMAND ----------
(
    monthly_customer_churn.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(GOLD_MONTHLY_CUSTOMER_CHURN)
)

row_count = spark.table(GOLD_MONTHLY_CUSTOMER_CHURN).count()
print(f"Wrote {row_count:,} rows to {GOLD_MONTHLY_CUSTOMER_CHURN}")

spark.table(GOLD_MONTHLY_CUSTOMER_CHURN).orderBy("city", "month").show(20, truncate=False)
