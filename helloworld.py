from flask import Flask
import pymongo
app = Flask(__name__)

@app.route('/')
def hello_puppy():
	return "Hello Empty"
	
@app.route('/flask')
def hello_flask():
   return "Hello Flask"

@app.route('/python/')
def hello_python():
   return "Hello Python"

if __name__ == '__main__':
   app.run()