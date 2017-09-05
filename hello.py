from flask import Flask, session, redirect, url_for, escape, request, render_template
from pymongo import MongoClient
import datetime
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
    return db,client

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    db,client = connect_to_db()
    datelist = db.users.find_one({'username': username}, {'timestamp':1})['timestamp']
    datelist = datelist[-5:]
    print datelist
    client.close()
    return render_template('userprofile.html', name=username, datelist = datelist)


@app.route('/', methods = ["GET","POST"])
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		db,client = connect_to_db()
		dict = db.users.find_one({'username': username}, {'username':1, 'password': 1})
		if dict:
			if dict['password'] == password:
				#session['username'] = request.form['username']
				update_dict = {}
				timestamp= datetime.datetime.now()
				db.users.find_one_and_update({'username': username},{'$push':{'timestamp': timestamp}, '$set':{'logged_in': True}})
				client.close()
				return redirect(url_for('show_user_profile', username='ankit'))			
		else:
			client.close()
			return "No such username registered with the website"
	else:
		return '''
			<form action = "" method = "post">
			<p>UserName: <input type ="text" name = "username"/></p>
			<p>Password: <input type ="password" name = "password"/></p>
			<p>Login: <input type = "submit" value = "Login"/></p>
			</form>
			'''

@app.route('/logout', methods = ["POST"])
def logout():
   # remove the username from the session if it is there

   if request.method == 'POST':
   		db,client = connect_to_db()
		#session.pop('username', None)
		print request.form['username']
		db.users.find_one_and_update({'username': request.form['username']},{'$set':{'logged_in': False}})
   		client.close()
   		return "logged out"




if __name__ == '__main__':
	app.run(debug=True)
