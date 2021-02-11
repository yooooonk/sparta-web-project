import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

client = MongoClient('localhost', 27017)
db = client.practice

soup = BeautifulSoup(data.text, 'html.parser')

lists = soup.select('#old_content > table > tbody > tr')
# old_content > table > tbody > tr:nth-child(6) > td.title > div > a

for tr in lists:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }

        db.movies.insert_one(doc)


