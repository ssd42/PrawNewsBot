#!/usr/bin/python
import smtplib
import GetNews
from email.mime.text import MIMEText
'''
This program uses the web crawling capabilities that praw allows to use
in order to retrieve five news article most relevant at the current time.
I chosen this method as Reddit's up vote system seems to consistently
choose relevant articles from reliable sources
'''

# Takes the emails and passwords necessary to send
# Values can be changed at any time
sender = 'mypybots@gmail.com'
password = ''
receivers = ['randommail@hastobegmail.com','mypybots@gmail.com']
username = 'mypybots'
subject = 'Daily dose of news'
timeframe = 12

# This is here for future purpose as this script will be on a
# Timeframe that it runs so one can get daily news.
# Might make a cron job later and run from a pie 
while True:

    # Initializes the Fetcher Class that uses Praw to grab the articles
    theNews = GetNews.GetNews()
    # Grabs a string containing the news and its respective link
    msg = theNews.mail_formating()

    text = MIMEText(msg.encode('utf-8'), 'plain', 'utf-8')
    # Converts from possible Unicode to avoid an encoding error

    text['From'] = sender
    text['To'] = ','.join(receivers)
    text['Subject'] = subject

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com:587')           # ('localhost', 1025)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receivers, text.as_string())
        smtpObj.quit()
        print("Successfully sent email")
    except Exception as e:
        print(e)
        print("Error: unable to send email")
    break    

