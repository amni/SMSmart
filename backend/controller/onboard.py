from base import Base
from models import User

class Onboard(Base):
    DEFAULT_ONBOARD_STRING ="""Welcome to SMSmart.
    Please blacklist this number for the best experience""" 

    def default(self, user, **kwargs):
        results = [DEFAULT_ONBOARD_STRING for x in range(5)]
        return results 
        