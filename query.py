from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["try"]
collection = database["geo_tag"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}

cursor = collection.find(query)
try:
    for doc in cursor:
        print doc["_id"]
finally:
    cursor.close()