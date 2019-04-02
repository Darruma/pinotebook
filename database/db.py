import sqlite3

conn = sqlite3.connect('notebook.db')

def create_table(schema):
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    with open(schema,'r') as file:
	    queries = file.read().split(".");
	    for query in queries:
		    c.execute(query)

def make_query(query):
	return conn.cursor().execute(query)

create_table("schema")

