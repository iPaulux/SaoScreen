import tweepy
import time
import shutil
import datetime
import os
from threading import Thread
import random

CONSUMER_KEY = 'wa6A1oqfsTLpLfywUHKSBlKXa'
CONSUMER_SECRET = 'LBUFZIVPbH0qrbvjU2EEIkFiRLCNf3LtDt659iRrCzP79FimyA'
ACCESS_KEY = '1307741217279672320-4At5rvPjoYgFt1EtxqziB6uIhrS4Pc'
ACCESS_SECRET = 'a6DV0nNbARDvumXiUy2xn46awBrKQoxHpVFsLou2yWDUf'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

        
FILE_NAME = '/home/pi/Desktop/my_bot/last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME) 
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#mysaocharacter' in mention.full_text.lower():
            print('found #mysaocharacter!')
            print('responding back...')
            a = random.choice(os.listdir("/home/pi/Desktop/my_bot/caracter"))
            filename = "/home/pi/Desktop/my_bot/caracter/{}".format(a)
            oldname = a[:-4]
            name = ''.join([i for i in oldname if not i.isdigit()])
            api.update_with_media(filename,"Your SAO character is {} !".format(name), in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True)

reply_to_tweets()
