from flask import Flask, session, redirect, url_for, escape, request
from pymongo import MongoClient
app = Flask(__name__)
 
 
'''
def index():

  		return 'Logged in as ' + username + '<br>' + \
			"<b><a href = '/logout'>click here to log out</a></b>"

  	return "You are not logged in <br><a href = '/login'></b>" + \
		"click here to log in</b></a>"
'''

def connect_to_db():
    # CreatePyMongoConnection
    client = MongoClient()
    db = client['test']
    return db



@app.route('/', methods = ["GET","POST"])
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		db = connect_to_db()
		dict = db.users.find_one({'username': username}, {'username':1, 'password': 1})
		if dict:
			if dict['password'] == password:
				return "logged in"
			return "lolled in"
		else:
			return "No such username registered with the website"
	else:
		return '''
			<form action = "" method = "post">
			<p>UserName: <input type ="text" name = "username"/></p>
			<p>Password: <input type ="password" name = "password"/></p>
			<p>Login: <input type = "submit" value = "Login"/></p>
			</form>
			'''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return "lol"




if __name__ == '__main__':
	app.run(debug=True)