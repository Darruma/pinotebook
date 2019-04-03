from flask import Flask,request,jsonify
from database.db import signup_user,login_user,create_days
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/signup/', methods=["POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        result = signup_user(data['username'],data['password'],data['email'])
        return result

signup_user('bob','poop','bob@gmail.com')
signup_user('steve','poopdescoop','mike@gmail.com')
create_days()