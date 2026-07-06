from src.utils.spark_session import get_spark_session

spark = get_spark_session()

print("Spark Version:", spark.version)

data = [
    ("AAPL", 190.45),
    ("MSFT", 425.80),
    ("GOOGL", 180.25),
]

df  = spark.createDataFrame(data, ["symbol", "price"])

df.show()

spark.stop()