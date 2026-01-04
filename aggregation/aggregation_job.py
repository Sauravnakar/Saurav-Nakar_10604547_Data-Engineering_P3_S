from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, sum

spark = SparkSession.builder.appName("AggregationJob").getOrCreate()

df = spark.read.parquet("/data/processed")

aggregated = df.groupBy("merchant").agg(
    count("*").alias("transaction_count"),
    avg("amt").alias("avg_amount"),
    sum("is_fraud").alias("fraud_count")
)

aggregated.write.mode("overwrite").parquet("/data/aggregated")

spark.stop()
