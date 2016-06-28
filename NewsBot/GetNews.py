import praw

r = praw.Reddit(user_agent='Daily_News')


class GetNews:


    # Need to find a way to fix to imports from a db.
    def __init__(self):
        # Data will be imported by from the db in future
        self.name_dic = {'news+worldnews': 5, 'askreddit': 2, 'jokes': 2, 'comics': 1}
        self.names = ['news+worldnews', 'askreddit', 'jokes', 'comics']
        self.need_description = {'news+worldnews': False, 'askreddit': False, 'jokes': True, 'comics': False}
        self.quantity = [3, 2, 1]
        self.the_message = ''

    # Function that grabs the data from reddit
    def get_top_stories(self, the_sub, amount=1):
        # To check if description is needed
        if self.need_description[the_sub]:
            gen_stor = r.get_subreddit(the_sub).get_top_from_day(limit=amount)
            news_dictionary = {a_thread.title: a_thread.selftext + '\n ------- \n' for a_thread in gen_stor}
            return news_dictionary
        # Otherwise send the shortlink
        else:
            gen_stor = r.get_subreddit(the_sub).get_top_from_day(limit=amount)
            news_dictionary = {a_thread.title: a_thread.short_link for a_thread in gen_stor}
            return news_dictionary

    # Formats the text simply to fit in the email.
    def mail_formatting(self, the_dict, sub_name):
        self.the_message += '\n' + sub_name.upper() + 2*'\n'
        # Just to add a title to each bunch of text
        for page in the_dict:
            self.the_message += page + '\t' + the_dict[page] + '\n'

    # Inputs might now be needed since can be grabbed from init
    def run_multiple_subreddits(self):
        for name in self.names:
            generated_dict_news = self.get_top_stories(name, self.name_dic[name])
            self.mail_formatting(generated_dict_news, name)

        return self.the_message

    # Function will be used to read from a db.
    # That way there will be no need to alter the
    # original file every time for a different person
    def get_from_database(self, db_name):
        with open(db_name, 'r') as database:
            for line in database:
                try:
                    name, amount = line.split('-')
                    self.name_dic[name] = amount
                    self.names.append(name)
                except ValueError:
                    print('Line could not be splitted ', line)


    # Just to make the sendNews cleaner and easier to read
    def get_mail_text(self):
        return self.run_multiple_subreddits()
