from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.practice

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']
    print(title, author, review)

    doc = {
        'title':title,
        'author':author,
        'review':review
    }

    db.bookreivew.insert_one(doc)

    return jsonify({'msg': '저장완료'})


@app.route('/review', methods=['GET'])
def read_reviews():

    reviews = list(db.bookreivew.find({},{'_id':False}))

    return jsonify({'reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)