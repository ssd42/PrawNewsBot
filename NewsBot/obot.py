import praw

app_ua = 'lern praw'
app_id = 'u5n0FAfmNA3PaA'
app_secret = 'SrQsLFWVh09TPtbw9gmTHHUhDqw'
app_uri = 'https://127.0.0.1:65010/authorize_callback'

app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'Xe32y13roppezbipKENyi9e_o6U'


app_refresh = '42769845-t-4lAOEzKIsKmaKvBuyQfYvaipA'


def login():
    r = praw.Reddit(user_agent = app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r
