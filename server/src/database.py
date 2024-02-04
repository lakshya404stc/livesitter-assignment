import pymongo
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/videostream?retryWrites=true&w=majority"
cluster = MongoClient('MONGO_URI')
db = cluster['videostream']