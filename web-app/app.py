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
    try:
        docs = db.userData.find({}, {"username": 1, "score": 1, "_id": 0}).sort('score',-1).limit(10)
        return render_template('leaderboard.html',docs=docs)
    # hello = list(docs)
    # print(hello)
    except:
        return render_template('leaderboard.html')


@app.route('/active')
def active():
    try:
        docs = db.userData.find({}, {"username": 1, "numLogins": 1, "_id": 0}).sort('numLogins',-1).limit(10)
        return render_template('active.html',docs=docs)
    except:
        return render_template('active.html')


@app.route('/comparison')
def comparison():
    try:
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
        
        plt.barh(objects,object_averages, color={'red','green','blue','orange','grey','brown','purple','yellow','indigo','violet'})
        plt.tight_layout(pad=3)
        plt.xlabel('Average scores')
        plt.ylabel('Objects')
        plt.title('Object Score Comparisons')
        plt.savefig('./static/images/plot.png')
        plt.clf()
        return render_template('comparison.html',url='./static/images/plot.png')
    except:
        return render_template('comparison.html',url='./static/images/plot.png')

@app.route('/statistics')
def statistics():
    try:
        docs = db.userData.find({}, {"baseball_bat": 1,"eyeglasses": 1,"grapes": 1,"anvil": 1,"laptop": 1,"dumbbell": 1,"sun": 1,"book": 1,"drums": 1,"ladder": 1})
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
        allScores=[]
        allScores.append(scoresForBaseballBat)
        allScores.append(scoresForEyeglasses)
        allScores.append(scoresForGrapes)
        allScores.append(scoresForAnvil)
        allScores.append(scoresForLaptop)
        allScores.append(scoresForDumbbell)
        allScores.append(scoresForSun)
        allScores.append(scoresForBook)
        allScores.append(scoresForDrums)
        allScores.append(scoresForLadder)
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
        listOfObjects=[]
        for i in range(10):
            failed,average,good,veryGood,excellent,perfect=countsScores(allScores[i])
            scores={}
            scores["object_name"]=objects[i]
            scores["failed"]=failed
            scores["average"]=average
            scores["good"]=good
            scores["veryGood"]=veryGood
            scores["excellent"]=excellent
            scores["perfect"]=perfect
            listOfObjects.append(scores)
        print(listOfObjects)
        return render_template('statistics.html')
    except:
        return render_template('statistics.html')

@app.route('/baseball')
def baseball():
    try:
        docs = db.userData.find({}, {"baseball_bat": 1})
        scoresForBaseballBat=[]
        for doc in docs:
            scoresForBaseballBat.append(doc["baseball_bat"])
            
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForBaseballBat)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Baseball Statistics')
        plt.savefig('./static/images/baseball.png')
        plt.clf()
        return render_template('display.html',url='./static/images/baseball.png')
    except:
        return render_template('display.html',url='./static/images/baseball.png')

@app.route('/eyeglasses')
def eyeglasses():
    try:
        docs = db.userData.find({}, {"eyeglasses": 1})
        scoresForEyeglasses=[]
        for doc in docs:
            scoresForEyeglasses.append(doc["eyeglasses"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForEyeglasses)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Eyeglasses Statistics')
        plt.savefig('./static/images/eyeglasses.png')
        plt.clf()
        return render_template('display.html',url='./static/images/eyeglasses.png')
    except:
        return render_template('display.html',url='./static/images/eyeglasses.png')

@app.route('/grapes')
def grapes():
    try:
        docs = db.userData.find({}, {"grapes": 1})
        scoresForGrapes=[]
        for doc in docs:
            scoresForGrapes.append(doc["grapes"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForGrapes)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Grapes Statistics')
        plt.savefig('./static/images/grapes.png')
        plt.clf()
        return render_template('display.html',url='./static/images/grapes.png')
    except:
        return render_template('display.html',url='./static/images/grapes.png')

@app.route('/anvil')
def anvil():
    try:
        docs = db.userData.find({}, {"anvil": 1})
        scoresForAnvil=[]
        for doc in docs:
            scoresForAnvil.append(doc["anvil"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForAnvil)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Anvil Statistics')
        plt.savefig('./static/images/anvil.png')
        plt.clf()
        return render_template('display.html',url='./static/images/anvil.png')
    except:
        return render_template('display.html',url='./static/images/anvil.png')

@app.route('/laptop')
def laptop():
    try:
        docs = db.userData.find({}, {"laptop": 1})
        scoresForLaptop=[]
        for doc in docs:
            scoresForLaptop.append(doc["laptop"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForLaptop)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Laptop Statistics')
        plt.savefig('./static/images/laptop.png')
        plt.clf()
        return render_template('display.html',url='./static/images/laptop.png')
    except:
        return render_template('display.html',url='./static/images/laptop.png')
    

@app.route('/dumbbell')
def dumbbell():
    try:
        docs = db.userData.find({}, {"dumbbell": 1})
        scoresForDumbbell=[]
        for doc in docs:
            scoresForDumbbell.append(doc["dumbbell"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForDumbbell)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Dumbbell Statistics')
        plt.savefig('./static/images/dumbbell.png')
        plt.clf()
        return render_template('display.html',url='./static/images/dumbbell.png')
    except:
        return render_template('display.html',url='./static/images/dumbbell.png')

@app.route('/sun')
def sun():
    try:
        docs = db.userData.find({}, {"sun": 1})
        scoresForSun=[]
        for doc in docs:
            scoresForSun.append(doc["sun"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForSun)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Sun Statistics')
        plt.savefig('./static/images/sun.png')
        plt.clf()
        return render_template('display.html',url='./static/images/sun.png')
    except:
        return render_template('display.html',url='./static/images/sun.png')

@app.route('/book')
def book():
    try:
        docs = db.userData.find({}, {"book": 1})
        scoresForBook=[]
        for doc in docs:
            scoresForBook.append(doc["book"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForBook)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Book Statistics')
        plt.savefig('./static/images/book.png')
        plt.clf()
        return render_template('display.html',url='./static/images/book.png')
    except:
        return render_template('display.html',url='./static/images/book.png')

@app.route('/drums')
def drums():
    try:
        docs = db.userData.find({}, {"drums": 1})
        scoresForDrums=[]
        for doc in docs:
            scoresForDrums.append(doc["drums"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForDrums)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Drums Statistics')
        plt.savefig('./static/images/drums.png')
        plt.clf()
        return render_template('display.html',url='./static/images/drums.png')
    except:
        return render_template('display.html',url='./static/images/drums.png')

@app.route('/ladder')
def ladder():
    try:
        docs = db.userData.find({}, {"ladder": 1})
        scoresForLadder=[]
        for doc in docs:
            scoresForLadder.append(doc["ladder"])
        failed,average,good,veryGood,excellent,perfect=countsScores(scoresForLadder)
        y=[]
        y.append(failed)
        y.append(average)
        y.append(good)
        y.append(veryGood)
        y.append(excellent)
        y.append(perfect)
        x=["Failed","Average","Good","Very Good","Excellent","Perfect"]
        plt.barh(x,y, color={'red','green','blue','orange','grey','brown'})
        plt.tight_layout(pad=3)
        plt.xlabel('Counts')
        plt.ylabel('Labels')
        plt.title('Ladder Statistics')
        plt.savefig('./static/images/ladder.png')
        plt.clf()
        return render_template('display.html',url='./static/images/ladder.png')
    except:
        return render_template('display.html',url='./static/images/ladder.png')

if __name__ == "__main__":
    PORT = os.getenv('PORT', 5000) # use the PORT environment variable, or default to 5000

    #import logging
    #logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(port=PORT)