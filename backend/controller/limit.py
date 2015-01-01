from base import Base
from models import User

class Limit(Base):
    def default(self, user, **kwargs):
        return {"messages":["text_limit:%d" % user.text_limit], "key": ''}