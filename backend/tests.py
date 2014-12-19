import app
import unittest
from models import User, Query

class TestDistribute(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_distribute(self):
        pass

class TestWikipedia(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_wiki_search(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ Wikipedia search: term: Ford limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: Ford limit: 3 key: z")        

    def test_wiki_search_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ Wikipedia search: term: Mercury limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: Mercury limit: 3 key: z")        
        print 'Query: @ Wikipedia search: term: zv#432v* limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: zv#432v* limit: 3 key: z") 

    def test_wiki_summary(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ Wikipedia summary: term: Ford limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia summary: term: Ford limit: 3 key: z")        

    def test_wiki_summary_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ Wikipedia summary: term: Mercury limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia summary: term: Mercury limit: 3 key: z")        
        print 'Query: @ Wikipedia summary: term: zv#432v* limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia summary: term: zv#432v* limit: 3 key: z") 


class TestYelp(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_yelp(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ yelp search : key: c longlat: true near: 37.2530787,-121.9049539 category: burgers' 
        print app.process_message(default_user, "@ yelp search : key: c longlat: true near: 37.2530787,-121.9049539 category: burgers")

    def test_yelp_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @Yelp: near: ff3e21 category: 2312ds key: z'        
        print app.process_message(default_user, "@Yelp: near: ff3e21 category: 2312ds key: z")

class TestMaps(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_maps(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ maps directions : key: d  to: Food  from: 37.2531484,-121.9049462 mode: driving'
        print app.process_message(default_user, "@ maps directions : key: e  to: Castro Street, Mountain View, CA  from: 37.253135,-121.904945 mode: driving")

    def test_maps_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ maps directions : key: d  to: fdsfs231  from: fdsf13 mode: driving'
        print app.process_message(default_user, "@ maps directions : key: d  to: fdsfs231  from: fdsf13 mode: driving")

class TestUnicode(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_unicode(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ maps directions : key: d  to: Food  from: 37.2531484,-121.9049462 mode: driving'
        print app.process_message(default_user, "@ maps directions : key: d  to: Food  from: 37.2531484,-121.9049462 mode: driving")
        print 
        print 
        print 'Query: @ wikipedia summary : key: ob term : Coursera  limit : 3'
        print app.process_message(default_user, "@ wikipedia summary : key: ob term : Coursera  limit : 3")        

class TestMain(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()

    def test_main(self):
        default_user = User.objects(phone_number="5734894023").first()
        print 'Query: @ Wikipedia search: term: Ford limit: 3 key: z'
        print app.process_message(default_user, "@ Wikipedia search: term: Ford limit: 3 key: z")
        print 
        print 
        print 'Query: @ Wikipedia summary: term: cars limit: 5 key: z'
        print app.process_message(default_user, "@ Wikipedia summary: term: cars limit: 5 key: z")
        print 
        print
        print 'Query: @Yelp search: limit: 1 longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z' 
        print app.process_message(default_user, "@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1")
        print 
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


if __name__ == "__main__":
    unittest.main()
