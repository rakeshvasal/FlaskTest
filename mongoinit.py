import pymongo

myclient = pymongo.MongoClient("mongodb+srv://rakeshvasal:20041992@cluster0-9x2sl.mongodb.net/test?retryWrites=true")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else :
  print("The database not exists.")