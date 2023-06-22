from pymongo import MongoClient

from config import DATABASE_NAME, COLLECTION_NAME

client = MongoClient()
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]



