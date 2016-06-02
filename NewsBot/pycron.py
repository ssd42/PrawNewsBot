import schedule
import time
import os
'''
Initially this will just support for daily tasks
'''
# Still trying to understand ordered dicts so untill then
# working with multiple lists

time_in_between = 15
path = 'C:/Users/Steven/GitProjects/PrawNewsBot/NewsBot/'
file_name = 'sendMail.py'
command = 'py'


'''
with open('paths', 'r') as the_paths:
    for line in the_paths:
        path = line
'''
def job():
    os.system('cd ' + path)
    os.system(command + ' ' + file_name)
    print('working')

# schedule.every().day.at('15:13').do(job)
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(time_in_between)

