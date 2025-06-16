import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

load_dotenv()

spark = SparkSession.builder \
    .appName('LoadtoSQL') \
    .getOrCreate()

df = spark.read.csv(r'data\processed\part-00000-b6b4ec24-5cf5-45f7-9e57-eb0ee7370d1b-c000.csv',
                    header=True, inferSchema=True)

# df.printSchema()

# JDBC details

jdbc_url = "jdbc:mysql://localhost:3306/stockDB"
table_name = "stocksdata"
username = os.getenv('USERNAME')
password = os.getenv("PASSWORD")
df.write \
    .format('jdbc') \
    .option('url',jdbc_url) \
    .option('driver','com.mysql.cj.jdbc.Driver') \
    .option('dbtable',table_name) \
    .option('user',username) \
    .option('password',password) \
    .mode('append') \
    .save()