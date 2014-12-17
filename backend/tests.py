import app
import unittest
from models import User, Query



class TestDistribute(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_distribute(self):
        app.distribute("+14086934876", "The Ford Motor Company (colloquially referred to as Ford) is an American multinational automaker headquartered in Dearborn, Michigan, a suburb of Detroit. It was founded by Henry Ford and incorporated on June 16, 1903. The company sells automobiles and commercial vehicles under the Ford brand and most luxury cars under the Lincoln brand. Ford also owns Brazilian SUV manufacturer, Troller, and Australian performance car manufacturer FPV.")


class TestParser(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()
    
    def test_process_message(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ Wikipedia search: term: Ford limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: Ford limit: 3 key: z")
        print 
        print 
        print 'Query: @ Wikipedia summary: term: cars limit: 5 key: z'
        print app.process_message(default_user, "@ Wikipedia summary: term: cars limit: 5 key: z")
        print 
        print
        print
        print
        print 'Query: @Yelp search: limit: 1 longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z' 
        print app.process_message(default_user, "@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1")
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
    
distribute = TestDistribute

if __name__ == "__main__":
    unittest.main()
