from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.practice

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['GET'])
def listing():
    articles = list(db.orders.find({},{'_id':False}))

    return jsonify({'data':articles})

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
    name = request.form['name'];
    address = request.form['address'];
    count = request.form['count'];
    phone = request.form['phone'];

    dbData = {
        'name':name,
        'address':address,
        'count':count,
        'phone':phone
    }

    db.orders.insert_one(dbData);

    return jsonify({'msg':'저장되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)