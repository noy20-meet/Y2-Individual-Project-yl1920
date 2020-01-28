from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

from database import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/',methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
	 	return render_template("home.html")
	else:
		username=request.form['uname']
		password=request.form['psw']
		users=query_all()

		for user in users:
			if username==user.name and password==str(user.password):
				return render_template("login.html")

		return render_template("home.html")




		# You get all users

		# you check in a for loop, if username and password are the same as user.username and user.password ( for user in users: )how to take the name from the database?


		

@app.route('/signup',methods=['GET', 'POST'])
def signup():
	username=request.form['uname']
	password=request.form['psw']
	add_user(password, username)
	return redirect(url_for("home"))
		

@app.route('/login')
def login():
	return render_template("login.html")

	



if __name__ == '__main__':
    app.run(debug=True)