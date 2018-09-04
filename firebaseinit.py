from flask import Flask, render_template, request, flash, redirect, url_for, session, logging	
from firebase import firebase
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import json
from functools import wraps


app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://androidone-43cbb.firebaseio.com/', None)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/testing')
def testing():
    return '<h1>This is another testing page</h1>'

# Dashboard
@app.route('/dashboard')
##@is_logged_in	
def dashboard():
	result = firebase.get('/users', None)
	# for x in result:
	# print(x)
	userList = []
	userdata=''
	for x, y in result.items():
		d_list = json.loads(y)
  	  	userList.append(userdata)

		
	return render_template('displayallusers.html',users=userList)


if __name__ == '__main__':
    app.run(debug=True)
