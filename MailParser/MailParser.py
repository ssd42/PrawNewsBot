from PrawNewsBot.DB_Manager.sql_handler import *
# Stuff for time



def decode_line(lin):
    import datetime

    global user
    line = str(lin).lower()
    print(line)
    # Later on check if the subject is correct.
    subject_here = False

    if 'from' in line:
        print('getting user')
        for word in line.split():
            if '@' in word:
                user = word[1:-1]
    elif 'subject' in line:
        for word in line.split():
            if 'redditnews' in word:
                subject_here = True
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
