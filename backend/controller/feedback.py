from base import Base
import api.wrapper.wikipedia_wrapper as wikipedia_wrapper
from models import Comment, User

class Feedback(Base):

    def default(self, user, **kwargs):
        return self.submit(user, **kwargs)

    def submit(self, user, **kwargs):
    	new_comment = Comment(content = kwargs["content"])
    	new_comment.save()
        user.comments.append(new_comment)
      	user.save()
        return {"messages" :[]}     
