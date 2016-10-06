# PrawNewsBot

Small python bot that uses the reddit api(praw) to send me daily news

Method chosen due to reddits upvote system. As people seem to normally vote the most well written articles
from each day and those that (usually are more relevant)

This was written using Python 3.4 and Praw 3.4 (later versions of praw now require a different method of Oauth so careful with that)
In order to work properly make sure that you are logged into the email account you will be sending from the emails from.

If the error persists, switch the email you wish to use to the default email on your default browser.

Email sending and recieving are done in SMTP and POP3 respectivly.
