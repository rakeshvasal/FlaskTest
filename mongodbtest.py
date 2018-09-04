from flask import Flask,render_template
import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
app = Flask(__name__)

##client = MongoClient()
##db = client.sampleDB

client = pymongo.MongoClient("mongodb+srv://rakeshvasal:pass%4067675%0A@rakesh1-9x2sl.gcp.mongodb.net/test?retryWrites=true")
db = client.test
try:
    info = client.server_info() # Forces a call.
    print("Connected")
except ServerSelectionTimeoutError:
    print("server is down.")

@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
   app.secret_key='secret123'
   app.run(debug=True)