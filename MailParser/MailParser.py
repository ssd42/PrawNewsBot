from PrawNewsBot.DB_Manager.sql_handler import *
import re
# Stuff for time



def decode_line(lin):
    import datetime

    global user
    line = str(lin).lower()
    print(line)
    # Later on check if the subject is correct.


    # This long if/else tree can be avoided with regex fix it

    if 'from' in line:
        print('getting user')
        for word in line.split():
            #thia ia because of the <> in the email. Wonder if regex can fix
            if '@' in word:
                user = word[1:-1]
    elif 'subject' in line:
        for word in line.split():
            if 'talk.admin' in word:
                # Ok how do I raise the ocassion that they want to talk to me
                # maybe just look at it directly and ask them to assign a Subject
                # if so use sendmail to mail me irectly... may lead to spam
                pass


    elif '$' in line:
        print('getting command')
        print(line)
        try:
            print('inside try statement')
            if '$addme' in line:
                print('Got to db statement')
                add_to_db(user)
            elif '$deleteme' in line:
                remove_to_db(user)
        except Exception as e:
            print('got here no clue whats wront' + str(e))
            with open('logger.txt', 'a') as logger:
                logger.write(str(e) + '\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + '\n')
