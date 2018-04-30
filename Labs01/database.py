from pymongo import MongoClient

uri = "mongodb://yenln:nhuyen2809@ds257589.mlab.com:57589/c4e17"
client = MongoClient(uri)

db = client.get_default_database()

blog=db["blog"]

post = {
    'title': "Hôm nay trời đẹp",
    'content': "Tôi ở nhà code"
}
# blog.insert_one(post)


all_post = blog.find()
for post in all_post:
    print(post)
