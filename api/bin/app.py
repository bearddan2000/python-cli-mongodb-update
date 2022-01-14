from pymongo import MongoClient
import pprint

def print_collection(msg, col):
    print("[INFO] Select all % s" % msg)
    for item in col.find():
        pprint.pprint(item)

client = MongoClient('db', 27017)

db = client.test

print("[INFO] Before Insert empty collection")
pprint.pprint(db.list_collection_names())

shiv = [{"name": "shiv"}, {"name": "short sword"}]

collection = db.weapon

collection.insert_many(shiv)

print("[INFO] After Insert 1 collection")
pprint.pprint(db.list_collection_names())

print_collection("before update", collection)

collection.update_one(
    {"name": "shiv"},
    {"$set": {"name": "pole"}}
)

print_collection("after update", collection)
