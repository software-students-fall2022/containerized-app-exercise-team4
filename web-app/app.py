from flask import Flask
from pymongo import MongoClient
from email import message
from flask import Flask, render_template, request, redirect, session, abort, url_for, make_response
import re

app=Flask(__name__)

connection = MongoClient('localhost', 27017)

db = connection['app']

users = db['users']

@app.route("/register.html", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user_email = request.form["email"]
        user_name = request.form["username"]
        user_password = request.form["password"]
        
        # Checking Validation
        valid_email = "([A-Z]|[a-z]|[0-9])+@([a-z]|[A-Z])+\.(([a-z]){2}|([a-z]){3})"
        validation = re.match(valid_email, user_email)

        if len(user_email) == 0 or validation is None:
            return render_template("register.html", message="Please enter valid email")
        if len(user_name) == 0:
            return render_template("register.html", message="Please enter valid username")
        if len(user_password) == 0:
            return render_template("register.html", message="Please enter valid password")

        if users.count_documents({'email': user_email}) == 0:
            new_user = {
                'email': user_email,
                'username': user_name,
                'password': user_password
            }
            
            users.insert_one(new_user)
            return render_template("register.html", message="Registered")
        else:
            return render_template("login.html", message="User account already exists")
    else:
        return render_template("register.html")

# ---- TEST INFO 
# email : test@email.com
# username : test 
# pass : 1234

@app.route("/")
@app.route("/login.html", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        
        # Validating
        valid_email = "([A-Z]|[a-z]|[0-9])+@([a-z]|[A-Z])+\.(([a-z]){2}|([a-z]){3})"
        validation = re.match(valid_email, user_email)

        if len(user_email) == 0 or validation is None:
            return render_template("login.html", message="Please enter valid email")
        if len(user_password) == 0:
            return render_template("login.html", message="Please enter valid Password")

        x = users.find_one({'email': user_email})
        if x is not None:
            if x['password'] == user_password:
                return render_template("login.html", message="Logged In")
            else:
                return render_template("login.html", message="Wrong Password")
        else:
            return render_template("login.html", message="Invalid Email")

    else:
        return render_template("login.html", message="")
    
if __name__ == '__main__':
    app.run(debug=True)