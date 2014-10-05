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
            return "Please make the text in the form of yelp search: near: (your location)"
        keywords = ["distance", "category"]
        optional_params = {}
        for keyword in keywords:
            if keyword in kwargs:
                optional_params[keyword] = kwargs[keyword]
        results = yelp_wrapper.query(kwargs["near"], **optional_params)
        if kwargs["format"] == "android":
                return '\n'.join([result.to_android_string() for result in results])
        self.store_results(user, results)
        return '\n'.join([result.to_string() for result in results])

    def store_results(self, user, results):
        for result in results:
            stored_result = Variable.objects(keyword = str(result.counter), program = "yelp", user = user).first()
            if stored_result:
                stored_result.value = result.to_string_verbose()
                stored_result.save()
            else:
                result = Variable(keyword = str(result.counter), value = result.to_string_verbose(), program = "yelp", user = user)
                result.save()
    
    def more(self, user, **kwargs):
        more_results = Variable.objects(keyword= "more", program = "yelp", user = user).first()
        if more_results:
            return self.spliced_results(user, more_results.value.split("\n"))
        return "No more results"


    def info(self, user, **kwargs):
        if not "place" in kwargs:
            return "Please make the text in the form of yelp info: place: (your location)"
        return Variable.objects(keyword = kwargs["place"], program = "yelp", user = user).first().value

    def help(self, user, **kwargs):
        return """
        \tHere are some example texts!
        To get restaurants near San Francisco, text - yelp: near: San Francisco, CA\n
        To get bars near San Francisco, text - yelp: near: San Francisco, CA category: bars\n
        To get bars within 0.1 miles the Mission District of San Francsico, text - yelp: near: Mission District, San Francisco distance: 5\n
        Don't forget to use colons!
        """
