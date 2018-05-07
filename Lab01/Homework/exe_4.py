from matplotlib import pyplot
from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (uri)

db = client.get_default_database()

a=0
b=0
c=0


if ref == "event":
    a =+ 1
elif ref == "ads":
    b =+ 1
elif ref == "wom":
    c =+ 1

counts = [a,b,c]

ref = ["event","ads","wom"]

pyplot.pie(counts, labels = ref, autopct="%.1f%%", shadow = True, explode=[0,0.2,0])
pyplot.title("usage")
pyplot.axis("equal")

pyplot.show()
