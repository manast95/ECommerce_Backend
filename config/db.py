from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017")

'''
Connects to local MongoDB instance by default.
Can also use MongoDB Atlas as well.
For MongoDB Atlas functionality, enter the necessary uri with username and password.
'''