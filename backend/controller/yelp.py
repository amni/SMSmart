from base import Base
import api.yelp.wrapper as yelp_wrapper
from models import Variable, User

class Yelp(Base):
    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def spliced_results (self, user, results):
        end_index = len(results)
        if len(results) > 5:
            end_index = 5
        spliced_results = "\n".join(results[:end_index])
        more_results = "\n".join(results[end_index:])
        if (more_results):
            more = Variable(keyword= "more", value = more_results, program = "yelp", user = user)
            more.save() 
        return spliced_results

    def search(self, user, **kwargs):
        if not "near" in kwargs:
            return "Please make the text in the form of yelp search: near: location"
        keywords = ["distance", "category"]
        optional_params = {}
        for keyword in keywords:
            if keyword in kwargs:
                optional_params[keyword] = kwargs[keyword]
        return yelp_wrapper.query(kwargs["near"], **optional_params)

    def more(self, user, **kwargs):
        more_results = Variable.objects(keyword= "more", program = "yelp", user = user).first()
        if more_results:
            return self.spliced_results(user, more_results.value.split("\n"))
        return "No more results"


    def info(self, user, **kwargs):
        pass