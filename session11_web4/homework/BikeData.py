from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://admin:<password>@database-buvxv.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

mmm = client.db_bike

Bike_Services = mmm["my_data_bike"]
