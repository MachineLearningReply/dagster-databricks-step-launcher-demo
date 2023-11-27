from dagster import op, asset
import requests
from pyspark.sql.functions import col
from pyspark.sql import SparkSession

# Downloads a CSV file containing full moon dates

FULL_MOON_DATES_URL = 'https://dbtlearn.s3.us-east-2.amazonaws.com/seed_full_moon_dates.csv'
CSV_FILE_PATH = "/dbfs/tmp/seed_full_moon_dates.csv"

@op
def full_moon_dates_op():
    """
    Downloads, processes, and saves full moon dates to a Delta table.
    """
    spark = SparkSession.builder.appName("FullMoonDates").getOrCreate()

    try:
        r = requests.get(FULL_MOON_DATES_URL, timeout=10)
        with open(CSV_FILE_PATH, "wb") as f:
            f.write(r.content)
    except requests.RequestException as e:
        print(f"Error while downloading the file: {e}")
        return

    full_moon_dates_df = spark.read.option("header", "true").csv("dbfs:/tmp/seed_full_moon_dates.csv")
    full_moon_dates_df = full_moon_dates_df.withColumn("full_moon_date", col("full_moon_date").cast("date"))
    full_moon_dates_df.write.format("delta").mode("overwrite").saveAsTable("hive_metastore.<DB_SCHEMA>.raw_full_moon_dates")

@asset(required_resource_keys={"databricks_step_launcher"})
def full_moon_dates_delta_table():
    full_moon_dates_op()
