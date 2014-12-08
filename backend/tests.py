import app
import unittest
from models import User, Query


class TestParser(unittest.TestCase):
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
        print 'Query: @ Wikipedia search: limit: summary: Ford sentences: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia search: limit: summary: Ford sentences: 3 key: z")
        print 
        print 
        print 'Query: @ Wikipedia: search: cars limit: 5 key: z'
        print app.process_message(default_user, "@ Wikipedia: search: cars limit: 5 key: z")
        print 
        print
        print 'Query: @Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z' 
        print app.process_message(default_user, "@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z")
        print 
        print 
        print 'Query: @Yelp: near: Durham, NC category: bars key: z'        
        print app.process_message(default_user, "@Yelp: near: Durham, NC category: bars key: z")
        print 
        print 
        print 'Query: @Maps directions: from: san jose, CA to: san francisco, CA key: z'        
        print app.process_message(default_user, "@Maps directions: from: san jose, CA to: san francisco, CA key: z")
        print 
        print
        print 'Query: @Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking'         
        print app.process_message(default_user, "@Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking")
        print 
        print 

    def test_parse_module(self):
        """Checks that the parser parses the first word correctly"""
        pass

    def test_distribute(self):
        """Checks that the parser parses handles distributed texting properly"""
        pass
    
if __name__ == "__main__":
    unittest.main()
