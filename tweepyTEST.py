import tweepy

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

