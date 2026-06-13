import os

BASE_PATH = os.getenv("SWIGGY_BASE_PATH", "/Users/pragyakatiyar/Documents/Swiggy_Pipeline")

LANDING_ORDERS = BASE_PATH + "/landing/orders"
LANDING_CUSTOMERS = BASE_PATH + "/landing/customers"
LANDING_DELIVERY = BASE_PATH + "/landing/delivery"
LANDING_RESTAURANTS = BASE_PATH + "/landing/restaurants"

ALL_LANDING_PATHS = [LANDING_ORDERS, LANDING_CUSTOMERS, LANDING_DELIVERY, LANDING_RESTAURANTS]

CHECKPOINT_ORDERS = BASE_PATH + "/checkpoints/orders"
CHECKPOINT_DELIVERY = BASE_PATH + "/checkpoints/delivery"
#checkpoints not needed for customers and restaurants as they will be batch processed.

# Bronze
BRONZE_ORDERS      = "swiggy.bronze.orders_raw"
BRONZE_DELIVERY    = "swiggy.bronze.delivery_raw"
BRONZE_RESTAURANTS = "swiggy.bronze.restaurants_raw"
BRONZE_CUSTOMERS   = "swiggy.bronze.customers_raw"

# Silver
SILVER_ORDERS      = "swiggy.silver.orders_clean"
SILVER_DELIVERY    = "swiggy.silver.delivery_clean"
SILVER_RESTAURANTS = "swiggy.silver.restaurants_clean"
SILVER_CUSTOMERS   = "swiggy.silver.customers_clean"

# Gold
GOLD_FACT_ORDERS      = "swiggy.gold.fact_orders"
GOLD_FACT_DELIVERY    = "swiggy.gold.fact_deliveries"
GOLD_DIM_RESTAURANT   = "swiggy.gold.dim_restaurant"
GOLD_DIM_CUSTOMER     = "swiggy.gold.dim_customer"
GOLD_AGG_DELIVERY_KPIS    = "swiggy.gold.agg_delivery_kpis"
GOLD_AGG_CITY_DEMAND      = "swiggy.gold.agg_city_demand"
GOLD_AGG_RESTAURANT_KPIS  = "swiggy.gold.agg_restaurant_kpis"

