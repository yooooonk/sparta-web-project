from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.practice

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({},{'_id':False}))

    return jsonify({'data':articles})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    url = request.form['url'];
    comment = request.form['comment'];

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    print(title, image, desc, comment);

    dbData = {
        'url':url,
        'title':title,
        'image':image,
        'desc':desc,
        'comment':comment
    }

    db.articles.insert_one(dbData);

    return jsonify({'msg':'저장되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)