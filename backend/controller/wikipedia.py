from base import Base
import api.wrapper.wikipedia_wrapper as wikipedia_wrapper
from models import User

class Wikipedia(Base):

    SEARCH_LIMIT = 5
    SUMMARY_LIMIT = 3

    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        return self.wikipedia_query("search", Wikipedia.SEARCH_LIMIT, **kwargs)        

    def summary(self, user, **kwargs):
        return self.wikipedia_query("summary", Wikipedia.SUMMARY_LIMIT, **kwargs)        

    def wikipedia_query(self, query_type, limit, **kwargs):
        try:
            key = kwargs["key"]
            results = ''      
            if "limit" in kwargs:
                limit = kwargs["limit"]
            results = getattr(wikipedia_wrapper, query_type)(summary, limit)
            results = key + "^" + results
        except:
            results = "Wikipedia Query Error: Please try with more specific query"
        return results   
