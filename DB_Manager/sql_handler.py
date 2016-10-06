import sqlite3
import datetime
import sys

db_name = 'users.db'
db_absolutePath = 'C:/Users/Steven/GitProjects/PrawNewsBot/DB_Manager/users.db'
logger_dir = 'C:/Users/Steven/GitProjects/PrawNewsBot/MailParser/logger.txt'


db_name = db_absolutePath


# Code is here in case I wish to pass arguments into this code later on.
# Remember this for future uses
if len(sys.argv) > 1:
    args = list(sys.argv)
    db_name = str(args[1])

# Function checks if a user is already in the database, if not logs it and goes to next one.
def add_to_db(user):
    if not is_in_db(user):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        user = str(user)

        # This convoluted thing that looks like crap is to prevent sqlinjections(even though im reading email)
        c.execute('INSERT INTO users (name, datetime) VALUES (?, ?)', (user,  current_time()))

        # c.execute("INSERT INTO users VALUES ?", args)
        conn.commit()
        conn.close()
    else:
        with open(logger_dir, 'a') as logger:
            logger.write('\nDATABASE ERROR: The user {} was already in the database.'.format(user))


def remove_to_db(user):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE name=?", (user,)) # Look if this prevents the sql inject
    conn.commit()
    conn.close()


# function checks if the current user is in the database
def is_in_db(user):

    connection = sqlite3.connect(db_name)
    cond = connection.cursor()
    cond.execute('SELECT * FROM users')
    data = cond.fetchall()
    organized_data = [data[i][0] for i in range(len(data))]
    if user in organized_data:
        return True

    else: return False


def current_time():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


'''
# code to interact with db'\s
while True:
    raw = input('name: ')
    if raw == 'quit':
        break
    elif raw == '' or raw is None:
        pass
    else: add_to_db(raw)

    toDel = input('to delete: ')
    remove_to_db(toDel)

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    print([i for i in data])
    c.close()
'''


'''
code to make a db
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("CREATE TABLE 'users' ('name' TEXT, 'datetime' TEXT);")
conn.commit()
conn.close()
'''