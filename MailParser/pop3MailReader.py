import poplib, email, time
from PrawNewsBot.MailParser import MailParser
# import getpass
# from email import parser
# getpass in case this is to be turned into a small module for me
# parser cause the method i have right now in sql_handler doesn't seem reliable

def main():
    # the_message = ''

    user = 'mypybots@gmail.com'
    Mailbox = poplib.POP3_SSL('pop.gmail.com')
    Mailbox.user(user)
    Mailbox.pass_('')
    numMessages = len(Mailbox.list()[1])
    for i in range(numMessages):
        for msg in Mailbox.retr(i+1)[1]:
            raw_msg = email.message_from_bytes(msg)

            MailParser.decode_line(str(raw_msg))

    Mailbox.quit()

if __name__ == '__main__':
    main()
