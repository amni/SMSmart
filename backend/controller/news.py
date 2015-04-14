from base import Base
import api.wrapper.news_wrapper as news_wrapper


class News(Base):

    def default(self, user, **kwargs):
        return self.feed(user, **kwargs)

    def feed(self, user, **kwargs):
        key = kwargs["key"]
        category = kwargs["category"]
    	tweets = news_wrapper.get_tweets(category) 
    	results = self.OK + key + self.CARROT_TOKEN + self.CARROT_TOKEN.join(tweets)
    	return self.split_result(results)

