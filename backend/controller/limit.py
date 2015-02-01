from base import Base
from models import User

class Limit(Base):
    def default(self, user, **kwargs):
    	key = kwargs["key"]
    	#change this from hardcoded to not hardcoded
        return {"messages":["(1/1)|%d" % user.text_limit], "key": "8%s" % key}