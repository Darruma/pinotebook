import sqlite3
from passlib.hash import sha256_crypt

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
        return response(True,c.lastrowid)
    else:
        print('err')
        return response(False,'Username already exists')

def signin_user(username,try_password):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT password from USER where username = ?",[username])
    correct_password = c.fetchone()
    if correct_password:
        if sha256_crypt.verify(try_password,correct_password):
            userid = c.lastrowid  
            return response(True,userid)
        else:
            print('err')
            return response(False,'Wrong password')
    else:
        return response(False,'Wrong username')