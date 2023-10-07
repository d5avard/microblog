import motor.motor_asyncio
from urllib.parse import quote_plus
from models.posts import Post
import os

user = os.environ['ENTRY_STORE_MONGO_USERNAME']
password = os.environ['ENTRY_STORE_MONGO_PASSWORD']
host = "microblog-database-1:27017/"
args = "?authMechanism=DEFAULT"
uri = "mongodb://%s:%s@%s?%s" % (quote_plus(user), quote_plus(password), host, args)

client = motor.motor_asyncio.AsyncIOMotorClient(uri)
database = client.microblog
collection = database.post

async def fetch_one_post(text):
    document = await collection.find_one({"text": text})
    return document

async def fetch_all_posts():
    posts = []
    cursor = collection.find({})
    async for document in cursor:
        posts.append(Post(**document))
    return posts

async def create_post(post):
    document = post
    result = await collection.insert_one(document)
    return document

async def remove_post(text):
    await collection.delete_one({"text": text})
    return True