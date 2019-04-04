import sqlite3
from passlib.hash import sha256_crypt
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

def create_days(date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT userid from User')
    userids = c.fetchall()
    for id in userids:
        c.execute('INSERT INTO Day VALUES (NULL,?,?)',[date,id[0]])
        conn.commit()
        create_schedule(c.lastrowid)
    

def create_schedule(day_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO Schedule VALUES (NULL,?)',[day_id])
    conn.commit()

def create_note(day_id,note):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO Notes VALUES (NULL,?,?)',[day_id,note])
    conn.commit()

def delete_note(note_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM Notes WHERE noteid = ?',[note_id])
    conn.commit()



def delete_goal(goal_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM Goals WHERE goalid = ?',[goal_id])
    conn.commit()

def create_goal(day_id,goal):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO Goals VALUES (NULL,?,?)',[day_id,goal])
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

