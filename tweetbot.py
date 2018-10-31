import tweepy
import time

API_KEY = "YOUR KEY"
API_SECRET = "YOUR KEY"

ACCESS_TOKEN = "YOUR KEY"
ACCESS_TOKEN_SECRET = "YOUR KEY"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

tweets = ['этот твит проплачен великодушным пожизненным диктатором', 
		  'pip вам не pip3',
		  'сегодня я пишу код кончиком языка со слабой типизацией' ]

for tweet in tweets:
    status = api.update_status(tweet)
    time.sleep(120)

