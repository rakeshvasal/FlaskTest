import pymongo
from pymongo import MongoClient
##myclient = pymongo.MongoClient("mongodb+srv://rakeshvasal:20041992@cluster0-9x2sl.mongodb.net/test?retryWrites=true")
client = pymongo.MongoClient("mongodb+srv://rakeshvasal:20041992@rakesh1-9x2sl.gcp.mongodb.net/test?retryWrites=true")
db = client.test
##mydb = myclient["mydatabase"]
##db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)
