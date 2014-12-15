from base import Base
import api.info.wikipedia_wrapper as wikipedia_wrapper
from models import User, Query

class Wikipedia(Base):
    SEARCH_LIMIT = 5
    SUMMARY_LIMIT = 3

    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        key = kwargs["key"]
        results = ''        
        term = kwargs["term"]
        if "limit" in kwargs:
            limit = kwargs["limit"]
        else:
            limit = Wikipedia.SEARCH_LIMIT
        result = wikipedia_wrapper.search(term, limit)
        results = "^".join(result)
        results = key + "^" + results
        #self.store_results(user, results) #for the shared feature 
        return results

    def summary(self, user, **kwargs):
        key = kwargs["key"]
        results = ''        
        summary = kwargs["term"]
        if "limit" in kwargs:
            sentences = kwargs["limit"]
        else:
            sentences = Wikipedia.SUMMARY_LIMIT
        results = wikipedia_wrapper.summary(summary, sentences)
        results = key + "^" + results
        #self.store_results(user, results) #for the shared feature 
        return results        

    def store_results(self, user, results):
        for result in results:
            stored_result = Variable.objects(keyword = str(result.counter), program = "wikipedia", user = user).first()
            if stored_result:
                stored_result.value = result.to_string_verbose()
                stored_result.save()
            else:
                result = Variable(keyword = str(result.counter), value = result.to_string_verbose(), program = "yelp", user = user)
                result.save()

