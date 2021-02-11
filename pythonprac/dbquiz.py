from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.practice

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})

matrix = db.movies.find_one({'title':'매트릭스'})

print(matrix)