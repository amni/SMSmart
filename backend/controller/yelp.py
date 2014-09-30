from api import Api

class Yelp(Api):
    #Program names - use decorators?
    def find_results(self, **kwargs):
        print kwargs.keys()
    	pass 
    def search(self, near, category, distance):
        pass
    def info(self):
        pass
    def more(self):
        pass


