import tweepy
from tweepy import OAuthHandler
from tweepy import API
# from keys import *

api = tweepy.API()

#TODO move this to import file
ckey = '1rCqxG5Edqb9P2LChRLThxsMX'
csecret = 'W7uixaeGVB81tRreIOd1EF4AwOKo2mg1jZXCNt92gppsE6doOZ'
atoken = '2882222243-9NWDvvePkXIkD7pvGtZRqXOJ2Fg4fHK6Mr0gYE3'
asecret = 'QOJBahHz0FSw1qSZSVWgs0wpFWFXgU07QwjPHS5IWQRkP'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = API(auth)


def get_tweets(news_handle = "BreakingNews"):
	try: 
		new_tweets = api.user_timeline(screen_name = news_handle, count=7)
		for tweet in new_tweets:
			pos = tweet.text.find("- @")
			if pos < 0: 
				pos = tweet.text.find("http")
			tweet.text = tweet.text[:pos]
		result = [tweet.text for tweet in new_tweets]
	except: 
		result = "1"
	return result 
