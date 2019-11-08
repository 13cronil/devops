
from urllib import request
from bs4 import BeautifulSoup as b

url = 'http://www.bbc.co.uk'
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

req = request.Request(url, headers=h)
with request.urlopen(req) as r:
    data = b(r, 'html.parser')

title = data.title.string

with open(r'/data/scrapedTitles', 'a') as f:
    f.write(title)

