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


@app.route('/login')
def login_controller():
	if request.method == 'POST':
		str_username = request.form['username']
		str_password = request.form['password']
		
	return render_template('login.html', error = error)	
    

@app.route('/login_page')
def login_page():
    return render_template('login.html')

# Dashboard
@app.route('/about')
def dashboard():
    userlist = []
    result = firebase.get('/users', None)
    for x, y in result.items():
        userdata = json.dumps(y)
        lastindex = userdata.rindex('}')
        userdata = userdata[:lastindex]
        userdata = userdata + " ,\"id\" : \"" + x + "\"}"
        print(userdata)
        d_list = json.loads(userdata)
        userlist.append(d_list)

    return render_template('displayallusers.html', users=userlist)


@app.route('/add_user', methods=['GET','POST'])
def add_user():
	form = Add_user_form(request.form)
	if request.method == 'POST' and form.validate():
		user = {}
		name = form.name.data
		username = form.username.data
		email = form.email.data
		password = form.password.data
		user['name'] = name
		user['username'] = username
		user['email'] = email
		user['password'] = password
		json_data = json.dumps(user)
		json_str = json.loads(json_data)
		result = firebase.post("/users", json_str)
		print(result)

	return redirect(url_for('dashboard'))

@app.route('/add_user_page')
def add_user_page():
	form = Add_user_form(request.form)
	return render_template('registration.html', form = form)


@app.route('/delete_user/<string:id>', methods=['POST'])
def delete_user(id):
    flash('Article Deleted', 'success')
    return redirect(url_for('dashboard'))


class Add_user_form(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('UserName', [validators.Length(min=1, max=50)])
    email = StringField('Email Address', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
