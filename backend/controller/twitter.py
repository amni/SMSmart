from base import Base
import api.wrapper.twitter_wrapper as twitter_wrapper

class Twitter(Base):
    def default(self, user, **kwargs):
        return self.feed(user, **kwargs)

    def feed(self, user, **kwargs):
        key = kwargs["key"]
        results = twitter_wrapper.get_twitter_feed(user)
        if self.is_error(results):
            return self.get_error_response(results, key)
        spliced_results = self.cut_results(user, key, results, 7)
        results = spliced_results[0]
        joined_results = self.CARROT_TOKEN.join(results)        
        cleaned_results = self.prepend_key(key, joined_results)
        return self.split_result(cleaned_results) 

    def tweet(self, user, **kwargs):
        key = kwargs["key"]
        message = kwargs["message"]
        twitter_wrapper.tweet_message(user, message)
        return {"messages" :[]}  

    def retweet(self, user, **kwargs):
        key = kwargs["key"]
        tweet_id = kwargs["tweet_id"]
        twitter_wrapper.retweet_message(user, tweet_id)
        return {"messages" :[]}   
