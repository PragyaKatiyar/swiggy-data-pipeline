from pyspark.sql import SparkSession
import pyspark.sql.types
import pyspark.sql.functions
import sys
import config

spark = SparkSession.builder \
    .appName("Swiggy_Pipeline") \
    .getOrCreate()