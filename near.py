from bson.objectid import ObjectId
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydbname

db.ProductData.update_one({
  '_id': ObjectId(p['_id'])
},{
  '$set': {
    'd.a': existing + 1
  }
}, upsert=False)