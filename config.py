cooldown = 120 # this is the amount of seconds the bot will wait between each message to prevent spam/shadowban, feel free to change it to fit your needs
headless = False # default to False so that you can inspect what is happening # either True or False, keep an eye for capitalization. If True the bot will run in headless mode, this option saves memory and it would run on any CLI-only server
messages = [ # list of messages that the bot will choose from to send. To prevent detection...fill as many messages as you want; the more the better
    '',
    '',
]
keywords = ['Hello'] # list of keywords to scrape Reddit usernames based on. The bot will check these keywords and scrape a list of Reddit usernames that made a comment using them.


data = list() # ! Do not touch, the bot will handle.
scrape_urls = list() # ! Do not touch, the bot will handle.
list_usernames = list() # ! Do not touch, the bot will handle.
usernames_sent = list() # ! Do not touch, the bot will handle.
unable_to_send = list() # ! Do not touch, the bot will handle.
dict_usernames = {} # ! Do not touch, the bot will handle.
