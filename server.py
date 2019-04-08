from flask import Flask,request,jsonify
from database.db import signup_user,signin_user,create_day,get_day_info
from datetime import date
import os 
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def hello():
    return "Hello"

@app.route('/signup/', methods=["POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        result = signup_user(data['username'],data['password'],data['email'])
        return jsonify(result)

app.route('/signin/',methods=['POST'])
def signin():
    if request.method == 'POST':
        result = signin_user(data['username'],data['password'])
        if result['success']:
            session['user'] = result['data']
            return jsonify(success=True,data='Signed in')
        else:
            return jsonify(success=False,data='Error , please try again')



bob_id = signup_user('bob','poop','bob@gmail.com')['data']
steve_id = signup_user('steve','poopdescoop','mike@gmail.com')['data']
print("here")
create_day(str(date.today()),bob_id)
get_day_info(bob_id)
