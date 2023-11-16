import tweepy
import time
import shutil
import datetime
import os
from threading import Thread
import random

CONSUMER_KEY = 'X'
CONSUMER_SECRET = 'X'
ACCESS_KEY = 'X'
ACCESS_SECRET = 'X'
BEARER_TOKEN = 'X'

#auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#client = tweepy.Client(BEARER_TOKEN)
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#oauth1_user_handler = tweepy.OAuth1UserHandler(
#    "API / wa6A1oqfsTLpLfywUHKSBlKXa", "API / LBUFZIVPbH0qrbvjU2EEIkFiRLCNf3LtDt659iRrCzP79FimyA",
#    callback="Callback / Redirect URI / URL here"
#)



client = tweepy.Client(
   consumer_key=CONSUMER_KEY,
   consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
   access_token_secret=ACCESS_SECRET
   )

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def screen():
    nb = "{}".format(i)
    print('Time to post !')
    filenameTW = "screen/ep{}/{}.jpg".format(e, nb)
    media_id = api.media_upload(filename=filenameTW).media_id_string
    client.create_tweet(media_ids=[media_id])
    


def variable(file_name):
    i_read = open(file_name, 'r')
    var = int(i_read.read().strip())
    i_read.close()
    var
    return var
    
def ecrire(file_name,valeur):
    i_write = open(file_name, 'w')
    i_write.write(str(valeur))
    i_write.close()

i = variable('variableI.txt')
e = variable('variableE.txt')
ep = variable('variableEP.txt')
s = variable('variableS.txt')



screen()
api.update_profile(description = 'Screenshots of SAO anime every 30 minutes in order. Currently on : Saison {} - Ep {} (Probably Spoil and NSFW) | Dev by @CallMePaulux'.format(s,ep))

if s==3:
    api.update_profile(description = 'Screenshots of SAO anime every 30 minutes in order. Currently on : Saison Alizication - Ep {} (Probably Spoil and NSFW) | Dev by @CallMePaulux'.format(ep))


if s==4:
    api.update_profile(description = 'Screenshots of SAO anime every 30 minutes in order. Currently on : Ordinal Scale - Extra Movie (Probably Spoil and NSFW) | Dev by @CallMePaulux')

if s==5:
    api.update_profile(description = 'Screenshots of SAO anime every 30 minutes in order. Currently on : Progressive - Aria of a Starless Night (Probably Spoil and NSFW) | Dev by @CallMePaulux')

r = i+1
TF = os.path.isfile('screen/ep{}/{}.jpg'.format(e,r))

if TF is True:
    i+=1

else:
    i = 0
    e += 1
    ep += 1
if e == 26 and s == 1:
    s+=1
    ep = 1
if e == 50 and s == 2:
    s+=1
    ep=1

if e==97 and s ==3: 
    s+=1
    ep=1
if e== 98 and s==4:
    ep=1
    s+=1

ecrire('variableI.txt',i)
ecrire('variableEP.txt',ep)
ecrire('variableE.txt',e)
ecrire('variableS.txt',s)
