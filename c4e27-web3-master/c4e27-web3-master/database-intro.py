from pymongo import MongoClient
from bson.objectid import ObjectId

# 1. Connect mongodb
mongo_uri = "mongodb+srv://admin:admin@c4e27-cluster-v9wvw.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# 2. Get / Create database
db_demo = client.test_database

# 3. Get / Create collection
first_collection = db_demo["my_collection"]

# 4. Create document
# game_document = {
#     "title": "ko biet",
#     "description": "ko biet luon",
# }

# # 5. Insert document
# first_collection.insert_one(game_document)

# 6. READ
# 6.1 READ all
# all_documents = first_collection.find()
# for document in all_documents:
#     print(document["title"])

# 6.2 READ one
# one_document = first_collection.find_one({"title": "LoL"})
# print(first_collection.find())

# 7. DELETE
# delete_document = first_collection.find_one({"_id": ObjectId("5c9cdd3c68a3ff2198c3de50")})
# first_collection.delete_one(delete_document)
# print(delete_document)


# if delete_document is not None:
#     first_collection.delete_one(delete_document)
#     print("Deleted Complete!")
# else:
#     print("Not found")

# 8. UPDATE

update_document = first_collection.find_one({"_id": ObjectId("5c9cdd4d68a3ff2644dea326")})
new_value = {"$set": {"title": "KHONG BIET"}}
first_collection.update_one(update_document, new_value)


