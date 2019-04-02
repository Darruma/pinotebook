from flask import Flask
from database.db import make_query
app = Flask(__name__)

print(make_query("SELECT * FROM User"))
@app.route('/')
def hello():
    return "Hello"