# swiggy-data-pipeline
# Swiggy Data Engineering Pipeline using PySpark & Databricks

## Project Overview

This project simulates a real-world food delivery platform like Swiggy and demonstrates how modern data engineering pipelines are built using PySpark, Delta Lake, and Databricks.

The pipeline processes order, delivery, restaurant, and customer data through a Medallion Architecture (Bronze → Silver → Gold) to create business-ready analytical datasets.

The project covers end-to-end data engineering concepts including data generation, ingestion, data cleansing, SCD Type 2 implementation, Delta Lake MERGE operations, and business KPI generation.

---

## Architecture

### Data Sources

The pipeline ingests data from four operational sources:

1. Orders
2. Deliveries
3. Restaurants
4. Customers

### Medallion Architecture

#### Bronze Layer

Stores raw data exactly as received from source systems.

Tables:

* orders_raw
* delivery_raw
* restaurants_raw
* customers_raw

Features:

* Auto Loader ingestion
* Schema enforcement
* Raw data preservation
* Checkpointing

---

#### Silver Layer

Cleans, validates, and standardizes raw data.

Tables:

* orders_clean
* delivery_clean
* restaurants
* customers

Transformations:

* Null handling
* Data type standardization
* Duplicate removal
* Business rule validation
* SCD Type 2 implementation for dimensions
* Delta MERGE operations

---

#### Gold Layer

Business-ready analytical tables used for reporting and dashboards.

Tables:

### Daily Revenue

Tracks revenue trends by date.

Metrics:

* Total Orders
* Total Revenue
* Average Order Value

### Restaurant KPI

Tracks restaurant performance.

Metrics:

* Orders per Restaurant
* Revenue per Restaurant
* Average Rating
* Cancellation Rate

### Delivery KPI

Tracks delivery operations.

Metrics:

* Average Delivery Time
* SLA Compliance
* Late Deliveries
* Delivery Agent Performance

### Customer Segments

RFM-based customer segmentation.

Segments:

* Champions
* Loyal
* At Risk
* Lost

### City Demand

Analyzes demand across cities and zones.

Metrics:

* Total Orders
* Revenue
* Unique Customers
* Unique Restaurants
* Average Order Value

---
## Orchestration

This pipeline is orchestrated via a Databricks Job with the following 
task dependency graph:

bronze_orders   ──┐
bronze_delivery ──┼──→ silver_facts ──┐
bronze_dims     ──┘                   ├──→ gold
                   silver_dims ───────┘

- Schedule: Daily at 1:00 AM IST
- Compute: Serverless
- Bronze tasks run in parallel
- Failure notifications sent via email

## Tech Stack

### Data Processing

* PySpark
* Delta Lake
* Databricks

### Storage

* Delta Tables
* Unity Catalog

### Programming

* Python

### Data Generation

* Faker
* Random
* JSON

---

## Project Structure

```text
Swiggy_Pipeline/
│
├── config/
│   └── config.py
│
├── data_generator/
│   └── generate_data.py
│
├── notebooks/
│   ├── 01_bronze_orders
│   ├── 02_bronze_delivery
│   ├── 03_bronze_dimensions
│   ├── 04_silver_facts
│   ├── 05_silver_dimensions
│   └── 06_gold
│
├── landing/
│   ├── orders/
│   ├── delivery/
│   ├── restaurants/
│   └── customers/
│
└── README.md
```

---

## Data Volume

Generated Dataset:

| Source      | Records |
| ----------- | ------: |
| Orders      |  10,000 |
| Deliveries  |   9,063 |
| Restaurants |     500 |
| Customers   |   2,000 |

---

## Final Pipeline Output

### Bronze Layer

| Table        |   Rows |
| ------------ | -----: |
| orders_raw   | 10,000 |
| delivery_raw |  9,063 |
| restaurants  |    500 |
| customers    |  2,000 |

### Silver Layer

| Table          |   Rows |
| -------------- | -----: |
| orders_clean   | 10,000 |
| delivery_clean |  9,063 |
| restaurants    |    500 |
| customers      |  2,000 |

### Gold Layer

| Table             |  Rows |
| ----------------- | ----: |
| daily_revenue     | 7,844 |
| restaurant_kpi    |   500 |
| delivery_kpi      |    91 |
| customer_segments |     4 |
| city_demand       |   340 |

---

## Key Concepts Implemented

* Medallion Architecture
* Delta Lake
* Auto Loader
* Structured Data Ingestion
* Delta MERGE
* SCD Type 2
* Data Quality Validation
* Window Functions
* Aggregations
* Customer Segmentation (RFM)
* Business KPI Generation

---

## Business Insights Generated

The pipeline enables analysis of:

* Revenue trends over time
* Top-performing restaurants
* Delivery performance and SLA compliance
* Customer loyalty segmentation
* Demand by city and zone
* Order value distribution
* Customer behavior patterns

---

## Learning Outcomes

Through this project, the following data engineering concepts were implemented and practiced:

* Building scalable ETL pipelines
* Designing Medallion Architecture
* Working with Delta Lake
* Managing Slowly Changing Dimensions
* Creating Gold-layer business metrics
* Developing production-style Databricks workflows
* Implementing data quality and governance practices

---

## Future Enhancements

* Databricks Workflows / Jobs -- Done
* Real-time Streaming with Kafka
* Airflow Orchestration
* Great Expectations Data Quality Checks
* Power BI / Tableau Dashboard Integration
* CI/CD using Databricks Asset Bundles

---

## Author

Pragya Katiyar

Senior Data Analyst | Aspiring Data Engineer

Tech Stack: PySpark, Databricks, Delta Lake, SQL, Python, AWS
