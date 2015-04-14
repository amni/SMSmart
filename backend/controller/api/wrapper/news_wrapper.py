import tweepy
from tweepy import OAuthHandler
from tweepy import API
# from keys import *

api = tweepy.API()

#TODO move this to import file
ckey = '1rCqxG5Edqb9P2LChRLThxsMX'
csecret = 'W7uixaeGVB81tRreIOd1EF4AwOKo2mg1jZXCNt92gppsE6doOZ'
atoken = '2882222243-kv5KE3Vd2Hl8MKinuC1RSGPqrMPNNPhAIOg4ZeO'
asecret = '51oNxJExMJTbrj73dyFZaFSZxG7SNYmKKN0KjwhhBmZTS'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = API(auth)

twitter_handles = {
    'general':'BreakingNews',
    'sports':'SportsCenter',
    'business':'WSJ',
    'entertainment':'gossipTF'
}

def get_tweets(category):
    try: 
        news_handle = twitter_handles.get(category, 'BreakingNews')
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
