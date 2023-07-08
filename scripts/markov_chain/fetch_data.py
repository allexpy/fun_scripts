import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("http://www.directlyrics.com/ed-sheeran-give-me-love-lyrics.html")

bsObj = BeautifulSoup(html, "lxml")

namelist = bsObj.find_all("div", {"class": "lyrics lyricsselect"})

text = ("".join([p.get_text() for p in namelist]))

file = open('workfile.txt', 'w')
file.write(text)
file.close()
file = open('workfile.txt', 'r')
for item in file:
    print(item)
file.close()

#print ("".join([p.get_text() for p in namelist]))