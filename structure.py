


import tweepy
import time
import shutil
import datetime
import os
from threading import Thread
import random

#See twitter API

CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def screen():
    nb = "{}".format(i)
    print('Time to post !')
    
   
        filename = "/home/pi/Desktop/my_bot/screen/ep{}/{}.jpg".format(e, nb)
    print(filename)
    api.update_with_media(filename)
   
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

i = variable('/home/pi/Desktop/my_bot/variableI.txt')
e = variable('/home/pi/Desktop/my_bot/variableE.txt')
ep = variable('/home/pi/Desktop/my_bot/variableEP.txt')
s = variable('/home/pi/Desktop/my_bot/variableS.txt')


api.update_profile('Sao Screen','https://twitter.com/Paulgttn' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Saison {} - Ep {} (Probably Spoil and NSFW) | Dev by @Paulgttn'.format(s,ep))
screen()

ecrire('/home/pi/Desktop/my_bot/variableI.txt',i)
ecrire('/home/pi/Desktop/my_bot/variableEP.txt',ep)
ecrire('/home/pi/Desktop/my_bot/variableE.txt',e)
ecrire('/home/pi/Desktop/my_bot/variableS.txt',s)
