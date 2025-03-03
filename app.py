#import os
import os
import pickle
from flask import Flask, render_template, request
import numpy as np
from myobject import MyObject
import pyspark.pandas as ps
from pyspark.sql import SparkSession


# os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'
# spark = SparkSession.builder.getOrCreate()



app = Flask(__name__)
# with open('pipeline_model.pkl', 'rb') as file:
#     model = pickle.load(file)

# business_df = ps.read_parquet("C:\\Users\\sweet\\Downloads\\small_business-20230531T134058Z-001\\small_business")


# def cosineSimilarity(vector1, vector2):
#     #  sum(A . B) / (sqrt(sum (A**2)  * sqrt(sum (B**2)))
#     numerator = np.dot(vector1, vector2)
#     denominator = np.sqrt(np.dot(vector1, vector1)) * np.sqrt(np.dot(vector2, vector2))
#     return float(numerator/denominator)

# def getRestaurantDetails(sim_rest):
#     restaurant_details = sim_rest.join(business_df, on='business_id', how = 'inner') \
#                                  .select(sim_rest.business_id, \
#                                        sim_rest.similarity_score, business_df.name, \
#                                        business_df.categories, business_df.stars_restaurant, business_df.review_count,
#                                        business_df.latitude, business_df.longitude)
#     return restaurant_details

@app.route('/')
def index():

    restaurants=['A','B','C']
    return render_template('template.html',restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True)


