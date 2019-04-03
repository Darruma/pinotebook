import sqlite3
from passlib.hash import sha256_crypt
from datetime import date
def connect_db():
    return sqlite3.connect('pibook.db')

def response(success,message):
    return {
        "success":success,
        "message":message
    }
def create_table(schema):
    conn = connect_db()
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    with open(schema,'r') as file:
		    c.executescript(file.read())
    conn.commit()

def create_days():
    print('creating days')
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT userid from User')
    userids = c.fetchall()
    d = str(date.today())
    print(userids)
    for id in userids:
        c.execute('INSERT INTO Day VALUES (NULL,?,?)',[d,id[0] ])
    conn.commit()

def signup_user(username,password,email):
    conn = connect_db()
    c = conn.cursor()
    # check if user with name already exists
    c.execute("SELECT * FROM User where username = ?",[username])
    users = c.fetchall() 
    # if a user without that username exists , add it to the database
    if not users:
        hashed_password = sha256_crypt.encrypt(password)
        c.execute("INSERT INTO User VALUES (NULL,?,?,?)",[username,hashed_password,email])
        conn.commit()
        return True
    else:
        return False

def login_user(username,try_password):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT password from USER where username = ?",[username])
    correct_password = c.fetchone()
    if correct_password:
        if sha256_crypt.verify(try_password,correct_password):
            return response(True,'Logged in')
        else:
            return response(False,'Wrong password')
    else:
        return response(False,'Wrong username')

        

    
create_table("schema")

