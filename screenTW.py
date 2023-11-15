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

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def screen():
    nb = "{}".format(i)
    print('Time to post !')
    filename = "/home/pi/Desktop/my_bot/screen/ep{}/{}.jpg".format(e, nb)
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



screen()
api.update_profile('Sao Screen','https://twitter.com/Paulgttn' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Saison {} - Ep {} (Probably Spoil and NSFW) | Dev by @CallMePaulux'.format(s,ep))

if s==3:
    api.update_profile('Sao Screen','https://twitter.com/Paulgttn' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Alicization - Ep{} (Probably Spoil and NSFW) | Dev by @CallMePaulux'.format(ep))

if s==4:
    api.update_profile('Sao Screen','https://twitter.com/Paulgttn' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Ordinal Scale - Extra movie (Probably Spoil and NSFW) | Dev by @CallMePaulux'.format(s,ep))
if s==4:
    api.update_profile('Sao Screen','https://twitter.com/Paulgttn' ,'Aincrad - Floor 22', 'Screenshots of SAO anime every 30 minutes in order. Currently on : Gun Gale Online - Ep {} (Probably Spoil and NSFW) | Dev by @CallMePaulux'.format(s,ep))

r = i+1
TF = os.path.isfile('/home/pi/Desktop/my_bot/screen/ep{}/{}.jpg'.format(e,r))

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

ecrire('/home/pi/Desktop/my_bot/variableI.txt',i)
ecrire('/home/pi/Desktop/my_bot/variableEP.txt',ep)
ecrire('/home/pi/Desktop/my_bot/variableE.txt',e)
ecrire('/home/pi/Desktop/my_bot/variableS.txt',s)
