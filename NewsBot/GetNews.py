import obot
# initializes obot a class containing my reddit information.
# It is no necessary to use this program as you can crawl through
# reddit using praw mostly without an issue, I just prefer to have my bot
# connected with a respective account
r = obot.login()

#use of multireddits might still be a better choice for news.


class GetNews:
    def __init__(self):
        self.subreddits = 'news+worldnews'
        self.total_stors = 5

    def get_top_stories(self):
        # Generator must be within the function as this way it keeps generating new after each request
        gen_stor = r.get_subreddit(self.subreddits).get_top_from_day(limit=self.total_stors)

        the_dic = {athread.title: athread.short_link for athread in gen_stor}
        # creates a dictionary with the title and url

        return the_dic

    def mail_formating(self):
        # Generates message that will be the email as a string
        a_dic = self.get_top_stories()
        msg = ''
        for keys in a_dic:
            msg += keys + '\t' + a_dic[keys] + '\n' + '\n'
        return str(msg)
    # In case of future implementation of a system that grabs multiple subreddits
    def run_multiple_subreddits(self, subreds):
        '''The code here will run mail formatting for each of the subreddits imputed
           it will then agregate all the strings into a single one that will consist of the email.
           In order to function however mail_formatting will have to be changed in that it should take and imput
           or Fetcher could be the base class and everytime someone requests their specific subreddits a new class
           can be created using most vals of Fetcher'''
        pass
