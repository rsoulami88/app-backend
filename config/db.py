from pymongo import MongoClient

Client = MongoClient("mongodb://MongoUser:mongo123@cluster0-shard-00-00-3uxhh.mongodb.net:27017,cluster0-shard-00-01-3uxhh.mongodb.net:27017,cluster0-shard-00-02-3uxhh.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = Client["usersapp"]
collection = db["users"]
