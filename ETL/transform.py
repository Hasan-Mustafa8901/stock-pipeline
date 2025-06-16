import os
import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date,col,lag,avg
from pyspark.sql.window import Window

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def spark_session(app_name):
       return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

def read_data():
       data_dir = os.path.join(os.getcwd(),'data','raw')
       csv_files = [os.path.join(data_dir,f) for f in os.listdir(data_dir) if f.endswith('.csv')]
       spark = spark_session('stockTransform')
       df = spark.read.csv(csv_files,header=True,inferSchema=True)
       print('\nData read successfully...\n')
       return df

def transform_data(df):
        # Removed first 2 rows 
        rows_to_remove = ['Ticker','Date']
        df = df.filter(~col('Price').isin(rows_to_remove))
        # Renamed Column Price to Date
        df = df.withColumnRenamed('Price','Date')
        # Changed the date format
        df = df.withColumn('Date',to_date(df['Date'],'yyyy-MM-dd'))
        numeric_columns = ['Close','High','Low','Open','Volume']
        for column in numeric_columns:
                df = df.withColumn(column,col(column).cast('double'))
        
        windowSpec = Window\
                .partitionBy('Ticker')\
                .orderBy('Date')
        
        df = df.withColumn('Prev_Close',lag('Close').over(windowSpec))
        df = df.withColumn('Daily_Return',(col('Close')-col('Prev_close')) / col('Prev_close'))
        
        df = df.withColumn('MA_7',avg('Close').over(windowSpec.rowsBetween(-6,0)))
        df = df.withColumn('MA_20',avg('Close').over(windowSpec.rowsBetween(-19,0)))
        print('\nData transformed successfully...\n')
        return df

def save_data(df):
       output_path = os.path.join(os.getcwd(),'data','processed')
       df.coalesce(1).write.csv(output_path,header=True,mode='overwrite')
       print('\nTransformed Data Saved data/processed')

# import glob
# import shutil

# # After Spark write
# df.coalesce(1).write.csv(output_path, header=True, mode='overwrite')

# # Find the part file
# part_file = glob.glob(f"{output_path}/part-*.csv")[0]
# shutil.move(part_file, f"{output_path}/transformed_stocks_data.csv")


if __name__ == '__main__':
       try:
        df = read_data()
        transformed_df = transform_data(df)
        save_data(transformed_df)
       except Exception as e:
              logger.error(e)
        
