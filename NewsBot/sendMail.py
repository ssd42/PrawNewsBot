#!/usr/bin/python
import smtplib
import GetNews
from email.mime.text import MIMEText
import time, logging

'''
This program uses the web crawling capabilities that praw allows to use
in order to retrieve five news article most relevant at the current time.
I chosen this method as Reddit's up vote system seems to consistently
choose relevant articles from reliable sources
'''
LOG_NAME = 'Error_Log.log'
logging.basicConfig(filename=LOG_NAME, level=logging.DEBUG)
# Code is here for future implementations.
email_list = []
with open('emails.txt') as emails:
    for email in emails:
        email_list.append(email)

# Takes the emails and passwords necessary to send
# Values can be changed at any time
sender = 'mypybots@gmail.com'
password = ''
receivers = email_list
username = 'mypybots'
subject = 'Daily dose of news'

# This is here for future purpose as this script will be on a
# Timeframe that it runs so one can get daily news.
# Might make a cron job later and run from a pie 

# Initializes the Fetcher Class that uses Praw to grab the articles
theNews = GetNews.GetNews()
# Grabs a string containing the news and its respective link
msg = theNews.get_mail_text()


def sendMail(email):
    text = MIMEText(msg.encode('utf-8'), 'plain', 'utf-8')
    # Converts from possible Unicode to avoid an encoding error

    text['From'] = sender
    text['To'] = email # ','.join(receivers)
    text['Subject'] = subject

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com:587')           # ('localhost', 1025)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, email, text.as_string())
        smtpObj.quit()
        print("Successfully sent email")
    except Exception as e:
        print("Error: unable to send email: {}".format(e))
        logging.debug(e)

for address in receivers:
    sendMail(address)
    ''' This code is mainly on the pi and is to be erased later on'''
    with open('logger.txt', 'a') as logger:
        logger.write('\n' + address + ' ' + str(time.ctime()) + '\n')
