from base import Base
import api.wrapper.yelp_wrapper as yelp_wrapper
from models import User, Query

class Yelp(Base):
    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        key = kwargs["key"]
        keywords = ["distance", "category", "limit"]
        optional_params = {}
        for keyword in keywords:
            if keyword in kwargs:
                optional_params[keyword] = kwargs[keyword]
            
        if "longlat" in kwargs and kwargs['longlat'].strip() == 'true':  
            longlat = kwargs["near"].split(',')
            query_results = yelp_wrapper.query_geo(float(longlat[0]), float(longlat[1]), **optional_params)
        else:
            query_results = yelp_wrapper.query(kwargs["near"], **optional_params)
        
        if self.is_error(query_results):
            return self.get_error_response(query_results, key)

        results = self.OK + key + self.CARROT_TOKEN + self.CARROT_TOKEN.join([result.to_android_string() for result in query_results])
        return self.split_result(results)

