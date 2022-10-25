import os
import sys
from pyspark.sql import SparkSession

def init(app_name = 'Main'):
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    spark = (
        SparkSession
            .builder
            .appName("PythonPi")
            .getOrCreate()
    )
    return spark
