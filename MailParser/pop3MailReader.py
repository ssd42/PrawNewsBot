import poplib, email, time
from PrawNewsBot.MailParser import MailParser
# import getpass
# from email import parser


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

            '''
        raw_email = b"\n".join(Mailbox.retr(i+1)[1])
        parsed_email = email.message_from_bytes(raw_email)
        print(parsed_email)
        '''
    Mailbox.quit()

if __name__ == '__main__':
    main()
