import os
import sys

# Path for spark source folder
#os.environ['SPARK_HOME']="C:/spark-1.3.1-bin-hadoop2.6"

# Append pyspark  to Python Path
sys.path.append("C:/spark-1.3.1-bin-hadoop2.6/python/")
os.environ['PYSPARK_SUBMIT_ARGS'] = 'pyspark-shell'

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print ("Successfully imported Spark Modules")

    sc = SparkContext('local')

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)