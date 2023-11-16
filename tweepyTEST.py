import tweepy

CONSUMER_KEY = 'wa6A1oqfsTLpLfywUHKSBlKXa'
CONSUMER_SECRET = 'LBUFZIVPbH0qrbvjU2EEIkFiRLCNf3LtDt659iRrCzP79FimyA'
ACCESS_KEY = '1307741217279672320-4At5rvPjoYgFt1EtxqziB6uIhrS4Pc'
ACCESS_SECRET = 'a6DV0nNbARDvumXiUy2xn46awBrKQoxHpVFsLou2yWDUf'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAFTnJgEAAAAA%2B%2F%2FkKIixlg8HNPtsZA2MDtFi6VE%3Dxw63DpECwKdEb32KnHawkUFfZAXesokOnRinRyiseWLSTboCre'

client = tweepy.Client(
   consumer_key=CONSUMER_KEY,
   consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
   access_token_secret=ACCESS_SECRET
   )

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


#response = client.create_tweet(text='Test updating...')
text = 'Coming back'
media_id = api.media_upload(filename='0.jpg').media_id_string
client.create_tweet(text=text, media_ids=[media_id])
print("Tweeted!")

print(media_id)

