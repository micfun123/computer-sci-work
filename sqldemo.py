import uuid
import sqlite3
from jose import jwt
from datetime import datetime, timedelta

# Create a connection to the database
conn = sqlite3.connect("example.db")
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS users (uuid INTEGER PRIMARY KEY, username TEXT, passwordhash TEXT, email TEXT, created_at DATETIME)"
)
cur.execute(
    "CREATE TABLE IF NOT EXISTS tokens (uuid INTEGER PRIMARY KEY, token TEXT, created_at DATETIME, valid INTEGER)"
)
conn.commit()
conn.close()


def read_users(username):
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()
    conn.close()
    return user


def check_email(email):
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cur.fetchone()
    conn.close()
    return user


def create_user(username, passwordhash, email):
    # if the user already exists, return false
    if read_users(username):
        return False
    elif check_email(email):
        return False
    else:
        conn = sqlite3.connect("example.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, passwordhash, email, created_at) VALUES (?, ?, ?, ?)",
            (username, passwordhash, email, datetime.now()),
        )
        conn.commit()
        conn.close()
        return True


# demo code
print(create_user("test", "test", "test"))
print(read_users("test"))
create_user("test")
