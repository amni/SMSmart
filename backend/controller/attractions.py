from base import Base
import api.wrapper.tripadvisor_wrapper as trip_wrapper
from models import Query, User

class Attractions(Base):
    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        if not "near" in kwargs:
            return "Please make the text in the form of attractions search: near: (your location)"
        results = trip_wrapper.query(kwargs["near"])
        if kwargs["format"] == "android":
                return "TripAdvisor | Search\n" + "\n".join([result.to_android_string() for result in results])
        return '\n'.join([result.to_string() for result in results])

    def help(self, user, **kwargs):
        return """      
        Here is an example text!
        To get attractions near San Francisco, you would text - attractions search: near: San Francisco, CA\n
        Don't forget to use colons!
        """
