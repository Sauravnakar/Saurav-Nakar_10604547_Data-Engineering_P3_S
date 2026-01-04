from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, datediff, current_date

spark = SparkSession.builder.appName("ProcessingJob").getOrCreate()

df = spark.read.csv(
    "/data/raw/credit_card_transactions.csv",
    header=True,
    inferSchema=True
)

# Timestamp conversion
df = df.withColumn(
    "transaction_time",
    to_timestamp("trans_date_trans_time")
)

# Derive age from dob
df = df.withColumn(
    "age",
    datediff(current_date(), col("dob")) / 365
)

# Basic validation
df = df.filter(col("amt") > 0)

df.write.mode("overwrite").parquet("/data/processed")

spark.stop()
