from base import Base
import api.yelp.wrapper as yelp_wrapper

class Yelp(Base):
    #Program names - use decorators?
    def default(self, **kwargs):
        return self.search(**kwargs)
    def search(self, **kwargs):
        return yelp_wrapper.query(kwargs['near'], kwargs['distance'])

    def info(self, **kwargs):
        pass
    def more(self, **kwargs):
        pass
