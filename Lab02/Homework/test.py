from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

raw_data = conn.read()
text = raw_data.decode("ISO-8859-1")

soup = BeautifulSoup(text,"html.parser")
s = soup.find("section","section chart-grid")
d = s.find("div","section-content")
ul= d.find("ul")

li_list=ul.find_all("li")
songs_list=[]

for li in li_list:
    a = li.h3.a
    b = li.h4.a
    song = a.string
    author = b.string

    data = {
            "Song"   : song,
            "Author" : author
        }
    data_list.append(data)
pyexcel.save_as(records = data_list, dest_file_name = "iTunesSongs.xlsx")
