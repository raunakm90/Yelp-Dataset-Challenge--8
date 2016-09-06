'@Author - Raunak Mundada'
'Date Created - 9/5/2016'

# Analyze the business data set

import sys
import pandas as pd
import numpy as np

from pymongo import MongoClient

def getMongoDB_client():
	client = MongoClient() # Connect to MongoDB
	return (client.yelp_db)

def getMongoDB_query():
	stars = list()
	yelp_db = getMongoDB_client()
	business = yelp_db.business
	doc_content = business.find()

	for item in doc_content:
		stars.append(item['stars'])

	return (stars)

if __name__ == '__main__':
	stars_list = getMongoDB_query()
	print (stars_list)
