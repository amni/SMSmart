from base import Base
import api.wrapper.news_wrapper as news_wrapper


class News(Base):

    def default(self, user, **kwargs):
        return self.feed(user, **kwargs)

    def feed(self, user, **kwargs):
        key = kwargs["key"]
    	tweets = news_wrapper.get_tweets() 
    	results = key + "^" + "^".join([tweet for tweet in tweets])
    	return self.split_result(results)

