from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from data import Articles  	
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import pymongo
app = Flask(__name__)

Articles = Articles()  	

@app.route('/')
def hello():
	return render_template('home.html')

@app.route('/registration', methods = ['GET', 'Post'])
def registration():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		return render_template('registration.html', form = form)	
	return render_template('registration.html', form = form)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html' , articles = Articles)

@app.route('/article/<string:id>')
def article(id):
	return render_template('article.html' , id=id)	

class RegistrationForm(Form):
	name = StringField('Name',[validators.Length(min = 1, max=50)])
	username = StringField('UserName',[validators.Length(min = 1, max=50)])
	email = StringField('Email Address',[validators.Length(min = 1, max=50)])
	password = PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm',message = 'Passwords donot Match')	
		])
	confirm = PasswordField('Confirm Password')

if __name__ == '__main__':
   app.run(debug=True)