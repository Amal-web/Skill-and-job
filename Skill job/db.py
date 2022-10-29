import sqlite3

con=sqlite3.connect("users.db")

print("successfullly connected");

con.execute("CREATE TABLE users (id TEXT, name TEXT,email TEXT,phone TEXT ,password TEXT)")

con.execute("CREATE TABLE userdata (name TEXT,about TEXT,email TEXT,phone TEXT, designation TEXT,school TEXT,skills TEXT,project TEXT,description TEXT)")
print("profile table created")

print("table created")
con.close()