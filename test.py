from pymongo import MongoClient
client = MongoClient()
db = client["db"]

users = db["twitter"]
#users.insert_one(dict(handle="trump", num_tweet="50", picture_urls=["img.img.com"], picture_labels=["cat", "dog"]))
cursor = users.find({})
for document in cursor:
      print(document)