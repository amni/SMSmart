from base import Base
from models import User

class Onboard(Base):
    DEFAULT_ONBOARD_STRING = ' Welcome to SMSmart. Please blacklist this number for the best experience.' 
    HARD_COUNT = 100

    def default(self, user, **kwargs):
    	boolean = "F" if self.get_user_count() > self.HARD_COUNT else "T" 
        results = [boolean + self.DEFAULT_ONBOARD_STRING for x in range(5)]
        return {"messages":results, "key": ''}

    def get_user_count(self):
    	return len(User.objects.all())
        