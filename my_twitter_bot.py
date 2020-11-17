import tweepy
import time
import shutil
import datetime
import os
from os import environ
from threading import Thread
import random

print("SAO Twitter bot")

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

        
FILE_NAME = 'last_seen_id.txt'

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
        if '#mysaocaracter' in mention.full_text.lower():
            print('found #mysaocaracter!')
            print('responding back...')
            a = random.choice(os.listdir("caracter"))
            filename = "caracter/{}".format(a)
            oldname = a[:-4]
            name = ''.join([i for i in oldname if not i.isdigit()])
            api.update_with_media(filename,"Your SAO caracter is {} !".format(name), in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True)



def screen():
    nb = "{}".format(i)
    print('Time to post !')
    filename = "screen/ep{}/{}.jpg".format(e, nb)
    api.update_with_media(filename)
    
    


    
i = 0
e = 1
s = 1
ep = 1
api.update_profile('Sao Screen ✘','https://twitter.com/PilouBinks' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Saison {} - Ep {}'.format(s,ep))
while True:
    screen()
    for b in range(30):
        reply_to_tweets()
        time.sleep(60)
    i+=1
    if e == 50:
        if i == 286:
            e+=1
            ep+=1
            i=0
    if e == 1 or 26 or 51 or 96:
        if i == 267:
            e+=1
            ep+=1
            i = 0
    if e == 25 or 39 or 42:
        if i == 266:
            e+=1
            ep+=1
            i=0
    if e == 72 or 74 or 78 or 84 or 87:
        if i == 265:
            e+=1
            ep+=1
            i = 0
    if e == 62 or 69 or 76:
        if i == 264:
            e+=1
            ep+=1
            i=0
    if e == 95:
        if i == 263:
            ep+=1
            e+=1
            i=0
    if e == 58:
        if i == 261:
            e+=1
            ep+=1
            i=0
    if e ==14:
        if i==256:
            e+=1
            ep+=1
            i=0
    if e == 49:
        if i == 255:
            e+=1
            ep+=1
            i=0
    if e == 24:
        if i== 252:
            e+=1
            ep+=1
            i=0
    if e == 16:
        if i ==251:
            e+=1
            ep+=1
            i=0
    if e == 2 or 6 or 7 or 12 or 15 or 18 or 20 or 21 or 23 or 40 or 43:
        if i == 250:
            e+=1
            ep+=1
            i = 0
    if e == 3 or 4 or 8 or 9 or 10 or 13 or 19 or 28 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 41 or 44 or 45 or 46 or 47 or 48:
        if i == 249:
            e+=1
            ep+=1
            i = 0
    if e == 5 or 11 or 17 or 22 or 29 or 54 or 59 or 60 or 63 or 67 or 79 or 92:
        if i ==248:
            e+=1
            ep+=1
            i=0
    if e == 27 or 53 or 55 or 56 or 57 or 61 or 65 or 66 or 70 or 73 or 77 or 80 or 81 or 83 or 86 or 93:
        if i ==247:
            ep+=1
            e+=1
            i=0
    if e == 75 or 82 or 88 or 89 or 94:
        if i == 246:
            ep+=1
            e+=1
            i=0
    if e == 64 or 68 or 71 or 85 or 90:
        if i == 244:
            ep+=1
            e+=1
            i=0
    if e == 52:
        if i==241:
            ep+=1
            e+=1
            i=0
    if e == 91:
        if i == 222:
            ep+=1
            e+=1
            i=0
            
    if e == 26:
        s+=1
        ep = 1
    if e == 50:
        s+=1
        ep = 1
        api.update_profile('Sao Screen ✘','https://twitter.com/PilouBinks' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Saison {} - Ep {}'.format(s,ep))
    
        
        


