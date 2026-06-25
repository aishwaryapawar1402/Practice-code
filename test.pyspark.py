
from pyspark.sql import SparkSession

spark = SparkSession.builder \
.appName("MyFirstSparkApp") \
.getOrCreate()

data = [("Laptop", 50000), ("Mobile", 20000), ("Tablet", 30000)]
columns = ["Product", "Price"]
df = spark.createDataFrame(data, columns)
df.show()

spark.stop()

print ("Hello From The New Branch!")
