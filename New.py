from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["try"]
collection = database["mar1"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {
	db.Spot.aggregate(
	[
	{$match: {spotter: "kk6dct"}},
	{$group: { _id : {
    year:{$year:"$spotReceivedTimestamp"},
    month:{$month:"$spotReceivedTimestamp"},
    day:{$dayOfMonth:"$spotReceivedTimestamp"}
    },
    count:{$sum: 1 }
  }
}
])
}

cursor = collection.find(query)
try:
    for doc in cursor:
        print doc["_id"]
finally:
    cursor.close()