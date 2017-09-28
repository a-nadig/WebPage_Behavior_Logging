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
    client = MongoClient("ds127044.mlab.com", 27044)
    db = client['adaptivewebdb']
    db.authenticate('admin', 'admin')
    return db,client

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    db,client = connect_to_db()
    datelist = db.users.find_one({'username': username}, {'timestamp':1})['timestamp']
    datelist = reversed(datelist)
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
				db.users.update_many({},{'$set':{'logged_in': False}})
				db.users.find_one_and_update({'username': username},{'$push':{'timestamp': timestamp}, '$set':{'logged_in': True}})
				client.close()
				return redirect(url_for('show_user_profile', username=username))			
		else:
			client.close()
			return "No such username registered with the website"
	else:
		return render_template('index.html') 

@app.route('/signup', methods = ["GET", "POST"])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		db,client = connect_to_db()
		dict = db.users.find_one({'username': username}, {'username':1, 'password': 1})
		if dict is None:
			out_object = {'username': username, 'password': password}
			db.users.insert_one(out_object)
			db.users.update_many({},{'$set':{'logged_in': False}})
			db.users.find_one_and_update({'username': username},{'$push':{'timestamp': datetime.datetime.now()}, '$set':{'logged_in': True}})
			client.close()
			return redirect(url_for('show_user_profile', username=username))			
		else:
			return "Username already exists in our records. please choose a different username"


		
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


@app.route('/stackoverflow/logs', methods = ["POST"])
def storeLogs():
	print "Phew"
	if request.method == 'POST':
		out_object = {}
		out_object['action'] = request.form['action']
		out_object['content'] = request.form['content']
		out_object['url'] = request.form['url']
		out_object['timestamp'] = request.form['timestamp']
		print out_object
		db,client = connect_to_db()
		db.users.find_one_and_update({'logged_in': True},{'$push':{'logs': out_object}})
		client.close()
		return 'True'
	return 'False'

@app.route('/visualizations', methods = ["GET"])
def getVisualizations():
	print "Inside visualizations"
	return render_template('visualizations.html')



if __name__ == '__main__':
	app.run(debug=True)
