
from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .master("local") \
        .appName("Hands-on PySpark on Google Colab") \
        .getOrCreate()
print(spark)
import pyspark
from pyspark.sql.functions import *
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
sqlContext = pyspark.SQLContext.getOrCreate(spark)
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")        


# Read JSON files locally
df_business = spark.read.json('C:\\Users\\sweet\\Downloads\\yelp_academic_dataset_business (1).json')
# df_review = spark.read.json('/path/to/yelp_academic_dataset_review.json')


# df_business = sqlContext.read.json('drive/MyDrive/Big data/yelp_academic_dataset_business.json')
# df_review = sqlContext.read.json('drive/MyDrive/Big data/yelp_academic_dataset_review.json')