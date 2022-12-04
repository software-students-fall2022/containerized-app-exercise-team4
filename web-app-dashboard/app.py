from flask import Flask, render_template, request, redirect, url_for, make_response
from dotenv import load_dotenv
from webfunctions import countsScores
import os
import pymongo
import datetime
from bson.objectid import ObjectId
import sys
import base64
from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
# instantiate the app
app = Flask(__name__)

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
load_dotenv()  # take environment variables from .env.

# turn on debugging if in development modeflas
if os.getenv('FLASK_ENV', 'development') == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# connect to the database
cxn = pymongo.MongoClient(os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[os.getenv('MONGO_DBNAME')] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    print(' *', "Failed to connect to MongoDB at", os.getenv('MONGO_URI'))
    print('Database connection error:', e) # debug'

# set up the routes

# route for the home page
@app.route('/')
def home():
    """
    Route for the home page
    """
    return render_template('index.html') # render the hone template

@app.route('/leaderboard')
def leaderboard():
    docs = db.userData.find({}, {"username": 1, "score": 1, "_id": 0}).sort('score',-1).limit(10)
    # hello = list(docs)
    # print(hello)
    return render_template('leaderboard.html',docs=docs)


@app.route('/active')
def active():
    docs = db.userData.find({}, {"username": 1, "numLogins": 1, "_id": 0}).sort('numLogins',-1).limit(10)
    return render_template('active.html',docs=docs)


@app.route('/comparison')
def comparison():
    docs = db.userData.find({}, {"username": 1,"baseball_bat": 1,"eyeglasses": 1,"grapes": 1,"anvil": 1,"laptop": 1,"dumbbell": 1,"sun": 1,"book": 1,"drums": 1,"ladder": 1, "_id": 0}).sort('numLogins',-1)
    total=0
    object_scores = [1,2,3,4,5,6,7,8,9,10]
    objects = ["baseball_bat", "eyeglasses", "grapes", "anvil", "laptop", "dumbbell", "sun", "book", "drums", "ladder"]
    scores = {"Failed": 0, "Average": 10, "Good": 20, "Very Good": 30, "Excellent": 40, "Perfect": 50}
    for doc in docs:
        object_scores[0] += scores[doc[objects[0]]]
        object_scores[1] += scores[doc[objects[1]]]
        object_scores[2] += scores[doc[objects[2]]]
        object_scores[3] += scores[doc[objects[3]]]
        object_scores[4] += scores[doc[objects[4]]]
        object_scores[5] += scores[doc[objects[5]]]
        object_scores[6] += scores[doc[objects[6]]]
        object_scores[7] += scores[doc[objects[7]]]
        object_scores[8] += scores[doc[objects[8]]]
        object_scores[9] += scores[doc[objects[9]]]
        total+=1
        
    object_averages = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(object_scores)):
        object_averages[i] = object_scores[i] / total
        
    tick_label = ["bb", "bb", "bb", "bb", "bb", "bb", "bb", "bb", "bb", "bb"]
    
    # x_pos = [0,1,4,7,10,13,16,19,22,25]
    plt.barh(objects,object_averages, color={'red','green','blue','orange','grey','brown','purple','yellow','indigo','violet'})
    plt.tight_layout(pad=3)
    plt.xlabel('Average scores')
    plt.ylabel('Objects')
    plt.title('Object Score Comparisons')
    plt.savefig('./static/images/plot.png')
    return render_template('comparison.html',url='./static/images/plot.png')

@app.route('/statistics')
def statistics():
    docs = db.userData.find({}, {"baseball_bat": 1,"eyeglasses": 1,"grapes": 1,"anvil": 1,"laptop": 1,"dumbbell": 1,"sun": 1,"book": 1,"drums": 1,"ladder": 1}).sort('numLogins',-1)
    scoresForBaseballBat=[]
    scoresForEyeglasses=[]
    scoresForGrapes=[]
    scoresForAnvil=[]
    scoresForLaptop=[]
    scoresForDumbbell=[]
    scoresForSun=[]
    scoresForBook=[]
    scoresForDrums=[]
    scoresForLadder=[]
    objects = ["baseball_bat", "eyeglasses", "grapes", "anvil", "laptop", "dumbbell", "sun", "book", "drums", "ladder"]
    for doc in docs:
        scoresForBaseballBat.append(doc[objects[0]])
        scoresForEyeglasses.append(doc[objects[1]])
        scoresForGrapes.append(doc[objects[2]])
        scoresForAnvil.append(doc[objects[3]])
        scoresForLaptop.append(doc[objects[4]])
        scoresForDumbbell.append(doc[objects[5]])
        scoresForSun.append(doc[objects[6]])
        scoresForBook.append(doc[objects[7]])
        scoresForDrums.append(doc[objects[8]])
        scoresForLadder.append(doc[objects[9]])
    
    return render_template('statistics.html')

if __name__ == "__main__":
    PORT = os.getenv('PORT', 5000) # use the PORT environment variable, or default to 5000

    #import logging
    #logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(port=PORT)  
    