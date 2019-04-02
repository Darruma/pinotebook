import sqlite3

def create_connection():
    conn = sqlite3.connect('notebook.db')
    return conn

def create_table(conn,schema):
    c = conn.cursor()
    with open(schema,'r') as file:
        c.execute(file.read())

conn = create_connection();
create_table(conn,"schema.sql")

