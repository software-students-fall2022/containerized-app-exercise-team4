from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from tensorflow.keras.models import load_model
from bson.objectid import ObjectId
from dotenv import dotenv_values
from quickdraw import *
import datetime
import pymongo
import sys
import os

model, classes = initialize()

app = Flask(__name__)
config = dotenv_values(".env")

# turn on debugging if in development mode
if os.getenv('FLASK_ENV', 'development') == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# connect to the database
cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    # render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/draw')
def game():
    return render_template('index.html')

@app.route('/puzzle')
def puzzle():
    return getObject(classes)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    return jsonify({ 'result': predict(model, classes, data['image'], data['category']) })

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user_name = request.form["username"]
        user_password = request.form["password"]
        
        # Checking Validation
        if len(user_name) == 0:
            return render_template("register.html", message="Please enter valid username")
        if len(user_password) == 0:
            return render_template("register.html", message="Please enter valid password")

        if db.users.count_documents({'username': user_name}) == 0:
            new_user = {
                'username': user_name,
                'password': user_password
            }
            db.users.insert_one(new_user)
            print('Inserted', file=sys.stderr) 
            return redirect(url_for('login'))
        else:
            return render_template("register.html", message="User account already exists")
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["username"]
        user_password = request.form["password"]
 
        x = db.users.find_one({'username': user_name})
        if x is not None:
            if x['password'] == user_password:
                return redirect(url_for('game'))
            else:
                return render_template("login.html", message="Wrong Password")
        else:
            return render_template("login.html", message="Invalid Username")
    else:
        return render_template("login.html", message="")

@app.route("/logout")
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)
