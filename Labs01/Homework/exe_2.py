from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (uri)

db = client.get_default_database()

blog=db["posts"]

post = {
    'title': "Test",
    'author': "Yenln",
    'content': "Post thử thôi, chả biết có được không!!!"
}

blog.insert_one(post)

# all_post = blog.find()
# for post in all_post:
#     print(post)
