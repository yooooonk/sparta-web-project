from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.practice


matrix = db.movies.find_one({'title':'매트릭스'},{'_id':False})
print(matrix)