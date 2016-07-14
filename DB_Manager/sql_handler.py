import sqlite3
import datetime

db_name = 'users.db'


def add_to_db(user):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    user = str(user)
    c.execute('INSERT INTO users (name, datetime) VALUES (?, ?)', (user,  current_time()))

    # c.execute("INSERT INTO users VALUES ?", args)
    conn.commit()
    conn.close()


def remove_to_db(user):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE name=?", (user,))
    conn.commit()
    conn.close()


def current_time():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

while True:
    raw = input('name')
    add_to_db(raw)

"""
code to make a db
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("CREATE TABLE 'users' ('name' TEXT, 'datetime' TEXT);")
conn.commit()
conn.close()
"""