#!/usr/bin/python
import smtplib
import GetNews
from email.mime.text import MIMEText
import time, logging
import sqlite3

# The logging system seems irrelevant
LOG_NAME = 'Error_Log.log'
logging.basicConfig(filename=LOG_NAME, level=logging.DEBUG)
# Code is here for future implementations.
email_list = []
"""
with open('emails.txt') as emails:
    for email in emails:
        email_list.append(email)

Function to fetch the emails.

This is all the code needed to load from the database
"""
conn = sqlite3.connect("../DB_Manager/users.db")
c = conn.cursor()

sql_data = c.execute("SELECT name FROM users")

# This is to turn the list o tuples into strings
name_list = [''.join(username) for username in sql_data]
print(name_list)

"""
Ok after this I have to split the lists

best way to do it would be:

it be done yo delete me
"""


# list compreehension to slip a list into n size
def splitList(listL, n):
    return [listL[i:i+n] for i in range(0, len(listL), n)]


# Takes the emails and passwords necessary to send
# Values can be changed at any time
sender = 'mypybots@gmail.com'
password = ''
#receivers = email_list
receivers = splitList(name_list, 100)  # this is due to 100 emails limit per email on smtp
username = 'mypybots'
subject = 'Daily dose of news'




# Initializes the Fetcher Class that uses Praw to grab the articles
# Better here to not be needed to do while iterating through receivers
theNews = GetNews.GetNews()
# Grabs a string containing the news and its respective link
msg = theNews.get_mail_text()

def send_message(receivers_list):
    text = MIMEText(msg.encode('utf-8'), 'plain', 'utf-8') # Double conversion otherwise bug
    # Converts from possible Unicode to avoid an encoding error
    # For some reason i have to encode it twice for MIMEText

    text['From'] = sender
    text['To'] =  'All of you wonderful people'   #', '.join(receivers)
    text['Subject'] = subject

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com:587')           # ('localhost', 1025)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receivers_list, text.as_string())
        smtpObj.quit()
        print("Successfully sent email")
    except Exception as e:                           # Something can go wrong from google's side or an update
        print("Error: unable to send email: {}".format(e))
        logging.debug(e)

# BIG NOTE
# Need to restructure this as each email can handle a max of 100 people per email
# Otherwise SMTP server wont't send the email

def main():
    print(receivers)
    # I have to  deal with 100+ emails on smtp
    for list in receivers:
        print(receivers)
        send_message(list)

# Not sure if I ever want to turn this into a module
if __name__ == '__main__':
    main()
    with open('logger.txt', 'a') as logger:
        ''' This code is mainly on the pi and is to be erased later on'''
        logger.write('\n' + ', '.join(receivers) + ' \n' + str(time.ctime()) + '\n')


