from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from tensorflow.keras.models import load_model
from dotenv import load_dotenv
from quickdraw import *
import datetime
import pymongo
import sys
import os

model, classes = initialize()

app = Flask(__name__)

cxn = pymongo.MongoClient("mongodb+srv://dixit:dixit123@cluster0.7vestnp.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    # db = cxn[os.getenv('MONGO_DBNAME')] # store a reference to the database
    db = cxn["userInfo"] # store a reference to the database
    print(' ', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    print('', "Failed to connect to MongoDB at", os.getenv('MONGO_URI'))
    print('Database connection error:', e) # debug'

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
    if(data['category'] == "baseball bat"):
        data['category'] = "baseball_bat"
    word, objscore, res, category, score2 = predict(model, classes, data['image'], data['category'])
    if(not data['test']):
        uri = "data:image/png;base64,%s" % data['image']
        if(category == "baseball_bat"):
            db.images.insert_one({   
                'uri': uri,
                'category': "baseball bat",
                'word': word
            })
        else:
            db.images.insert_one({   
                'uri': uri,
                'category': category,
                'word': word
            })
        wordDict = {'Failed': 0, 'Average': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4, 'Perfect': 5}
        x = db.userData.find_one({'username': user_name})
        try:
            if ((x[category] == '') or (wordDict[x[category]] < wordDict[word])):
                db.userData.update_one(
                    {'username': user_name},
                    {'$set': {category: word}}
                )
            if (x['score'] < score2):
                db.userData.update_one(
                    {'username': user_name},
                    {'$set': {'score': score2}}
            )
        except Exception as e:
            print("error:", e)
    return jsonify(
        {
            'result': res,
            'score': objscore
        })

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        global user_name
        user_name = request.form["username"]
        user_password = request.form["password"]

        # Checking Validation
        if len(user_name) == 0:
            return render_template("register.html", message="Please enter valid username")
        if len(user_password) == 0:
            return render_template("register.html", message="Please enter valid password")

        if db.userData.count_documents({'username': user_name}) == 0:
            new_user = {
                'username': user_name,
                'password': user_password,
                'baseball_bat': 'Failed',
                'eyeglasses': 'Failed',
                'grapes': 'Failed',
                'anvil': 'Failed',
                'laptop': 'Failed',
                'dumbbell': 'Failed',
                'sun': 'Failed',
                'book': 'Failed',
                'drums': 'Failed',
                'ladder': 'Failed',
                'score': 0,
                'numLogins': 0
            }
            db.userData.insert_one(new_user)
            return redirect(url_for('login'))
        else:
            return render_template("register.html", message="User account already exists")
    else:
        return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        global user_name
        user_name = request.form["username"]
        user_password = request.form["password"]

        x = db.userData.find_one({'username': user_name})
        if x is not None:
            if x['password'] == user_password:
                db.userData.update_one(
                    {'username': user_name},
                    {'$set': {'numLogins': x['numLogins'] + 1}}
                )
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

if __name__ == "__main__":
    #import logging
    #logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(port=5000)
