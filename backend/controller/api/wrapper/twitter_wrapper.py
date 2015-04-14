import tweepy

auth = tweepy.OAuthHandler("1rCqxG5Edqb9P2LChRLThxsMX", "W7uixaeGVB81tRreIOd1EF4AwOKo2mg1jZXCNt92gppsE6doOZ")



def setup_auth(user):
	#api.set_access_token("user tokens")
	auth.set_access_token(user.get_auth("twitter").access, user.get_auth("twitter").secret)
	api = tweepy.API(auth)
	return api 

def get_twitter_feed(user):
	try:
		api = setup_auth(user)
		public_tweets = api.home_timeline(count=50)
		result = ["||".join([tweet.author.screen_name, tweet.text, str(tweet.id)]) for tweet in public_tweets]
	except: 
		result = "1"
	return result 

def tweet_message(user, message):
	try: 
		api = setup_auth(user)
		api.update_status(message)
		result = "0"
	except:
		result = "1"
	return result

def retweet_message(user, message_id):
	try: 
		api = setup_auth(user)
		api.retweet(int(message_id))
		result = "0"
	except:
		result = "1"
	return result 
