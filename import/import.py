import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.test_db
collection = db.test_coll

post = {"author": "Kristen",
	"text": "First post",
	"date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

