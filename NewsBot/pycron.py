import schedule
import time
import os
'''
Now supports multiple tasks
You could save as a pyc file if having the command line show up is unplesant (I believe)
'''
# Still trying to understand ordered dicts so until then
# working with multiple lists

time_in_between = 15
directory = 'C:/Users/Steven/GitProjects/PrawNewsBot/NewsBot/'
name = 'sendMail.py'
# by default it's set up for running other python files
com = 'py'


# opens up the cron file to get each commands from it.
def choose(file_name):
    with open(file_name) as command_file:
        for line in command_file:
            try:
                global name
                cron_coms = line.split(' ')
                frequency = cron_coms[0]
                number = cron_coms[1]
                command = cron_coms[2]
                path = cron_coms[3]
                name = cron_coms[4]
                set_schedule(frequency, number, command, path)
            # In case someone screws up their commands (didn't put muh thought into it yet)
            except Exception as e:
                print('There was an Error: \n {}'.format(e))


# Checks what command the user inputed and sets up the command accordingly
def set_schedule(frequency, number, command, path):
    try:
        int_number = int(number)

        if frequency == 'daily':
            schedule.every().day.at(int_number).do(job(command, path))
        elif frequency == 'hourly':
            schedule.every(int_number).hours.do(job(command, path))
        elif frequency == 'minute':
            schedule.every(int_number).minutes.do(job(command, path))
        elif frequency == 'weekly':
            schedule.every(int_number).weeks.do(job(command, path))
        else:
            print('{} is not a valid command'.format(frequency))
    except ValueError:
        print('Could not convert {} into an integer'.format(number))
    except Exception as e:
        print('There was an Error: \n {}'.format(e))


def job(command, path):
    os.system('cd ' + path)
    os.system(command + ' ' + name)
    print('Job went through.')


def main():
    while True:
        schedule.run_pending()
        time.sleep(time_in_between)


if __name__ == '__main__':
    main()
