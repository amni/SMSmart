import app
import unittest
from models import User, Query


class TestWiki(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()

    """def test_yelp_splitting(self):
        default_user = User.objects(phone_number="5734894023").first()
        output = app.process_message(default_user, "@ Yelp search:  longlat: true near: 36.0053098,-78.9260807 category: Food key: l")
        app.distribute("4086934876", output)"""

    def test_process_message(self):
        default_user = User.objects(phone_number="5734894023").first()
        """print 'Query: @ Wikipedia summary: term: Barack Obama limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia summary: term: Barack Obama limit: 3 key: z")
        print 
        print 
        print 'Query: @ Wikipedia search: term: Barack Obama limit: 5 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: Barack Obama limit: 5 key: z")
        print 
        print 
        print 'Query: @ Wikipedia search: term: James Buchanan Duke limit: 5 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: James Buchanan Duke limit: 5 key: z")
        print""" 
        print         
        print 'Query: @ wikipedia: summary : Philip Seymore Hoffman  sentences : 3  key: q'
        print app.process_message(default_user, "@ wikipedia summary: term: Philip Seymore Hoffman  limit: 3  key: q")        

    def test_parse_module(self):
        """Checks that the parser parses the first word correctly"""
        pass

    def test_distribute(self):
        """Checks that the parser parses handles distributed texting properly"""
        pass
    
if __name__ == "__main__":
    unittest.main()
