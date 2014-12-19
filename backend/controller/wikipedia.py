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

    def wikipedia_query(self, query_type, query_limit, **kwargs):
        key = kwargs["key"]
        results = ''      
        term = kwargs["term"]  
        if "limit" in kwargs:
            query_limit = kwargs["limit"]
        results = getattr(wikipedia_wrapper, query_type)(term, query_limit)
    
        if self.is_error(results):
            result = results + key + "^" + self.EMPTY_MSG
            return self.split_result(result)

        results = self.OK + key + "^" + results
        return self.split_result(results)   
