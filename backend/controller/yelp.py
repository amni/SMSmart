from base import Base
import api.wrapper.yelp_wrapper as yelp_wrapper
from models import User, Query

class Yelp(Base):
    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        key = kwargs["key"]
        if not "near" in kwargs:
            return "Please make the text in the form of yelp search: near: (your location)"
        keywords = ["distance", "category", "limit"]
        optional_params = {}
        for keyword in keywords:
            if keyword in kwargs:
                optional_params[keyword] = kwargs[keyword]
        if "longlat" in kwargs: 
            longlat = kwargs["near"].split(',')
            try:
                results = yelp_wrapper.query_geo(float(longlat[0]), float(longlat[1]), **optional_params)
            except:
                return "Yelp Search Error: Try searching with a named location instead of coordinates"
        else:
            results = yelp_wrapper.query(kwargs["near"], **optional_params)
        if kwargs["format"] == "android":
                return key + "^" + "^".join([result.to_android_string() for result in results])
        return '^'.join([result.to_string() for result in results])

