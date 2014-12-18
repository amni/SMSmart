from base import Base
from models import User, Query

class Share(Base):
    def default(self, user, **kwargs):
        for query in user.queries:
        	if query.query_id = kwargs[rid]:
        		return [query.response]
