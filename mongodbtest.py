from flask import Flask,render_template
import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import urllib

app = Flask(__name__)

##client = MongoClient()
##db = client.sampleDB

##app.config[] = ''
##app.config[] = ''

mongo_uri = "mongodb+srv://rakeshvasal:" + urllib.parse.quote("pass@67675")+"@rakesh1-9x2sl.gcp.mongodb.net/test?retryWrites=true"
client = pymongo.MongoClient(mongo_uri)

db = client.test

db.getSiblingDB("test").getCollection("foo").insert( { "msg" : "My First Document" } )
try:
    info = client.server_info() 
    print("Connected")
except ServerSelectionTimeoutError:
    print("server is down.")



@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
   app.secret_key='secret123'
   app.run(debug=True)