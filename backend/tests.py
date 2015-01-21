import app
import unittest
from models import User, Query


class BaseTest(unittest.TestCase):
    CARROT_SEPARATOR = '^^'
    PIPE_SEPARATOR = '||'

    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def basic_test(self, response, status_code):
        self.assertEqual(response['key'][:1], status_code)
        self.assertIsNotNone(response['messages'])
        self.assertIsInstance(response['messages'], list) 

    def separator_test(self, response, separator):
        messages = response['messages']
        self.assertTrue(self.check_separator(messages, separator))

    def check_separator(self, messages, separator):
        check = False
        for msg in messages:
            if separator in msg:
                check = True
        return check         

class TestNews(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_news(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ news feed: key: a")
        self.basic_test(response, '0')  
        self.separator_test(response, self.CARROT_SEPARATOR)

class TestSearch(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_search(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ search query: term: android key: a")
        self.basic_test(response, '0')  
        self.separator_test(response, self.PIPE_SEPARATOR)

class TestWeather(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_weather(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ weather search: near: london,uk key: a")
        self.basic_test(response, '0') 
        self.separator_test(response, self.PIPE_SEPARATOR)

class TestStock(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_stock(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ stock search: symbol: goog key: a")
        self.basic_test(response, '0')  
        self.separator_test(response, self.PIPE_SEPARATOR)

class TestOnboard(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_onboard(self):
        default_user = User.objects(phone_number="5734894023").first()
        onboard = app.process_message(default_user, "@Onboard")
        expected_onboard_msg = 'T||Welcome to SMSmart. Please blacklist this number for the best experience.'
        self.assertIsInstance(onboard['messages'], list)
        for msg in onboard['messages']:
            self.assertEqual(msg, expected_onboard_msg)


class TestWikipedia(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_wiki_search(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ Wikipedia search: term: Ford key: z")        
        self.basic_test(response, '0')   
        self.separator_test(response, self.CARROT_SEPARATOR)
        response = app.process_message(default_user, "@ Wikipedia search: term: zv#432v* limit: 3 key: z") 
        self.basic_test(response, '0')  
        response = app.process_message(default_user, "@ Wikipedia search: term: Mercury limit: 3 key: z")
        self.basic_test(response, '0')         
        self.separator_test(response, self.CARROT_SEPARATOR)

    def test_wiki_limit(self):
        default_user = User.objects(phone_number="5734894023").first()     
        response = app.process_message(default_user, "@ Wikipedia search: term: Mercury limit: 10000 key: z")
        self.basic_test(response, '0')    
        self.separator_test(response, self.CARROT_SEPARATOR)
        response = app.process_message(default_user, "@ Wikipedia search: term: Mercury limit: -2 key: z")
        self.basic_test(response, '0') 
        response = app.process_message(default_user, "@ Wikipedia summary: term: Coursera limit: -2 key: z")  
        self.basic_test(response, '0')  
        self.separator_test(response, self.PIPE_SEPARATOR)
        response = app.process_message(default_user, "@ Wikipedia summary: term: Coursera limit: 10000 key: z")  
        self.basic_test(response, '0')  
        self.separator_test(response, self.PIPE_SEPARATOR)        

    def test_wiki_summary(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ Wikipedia summary: term: Ford limit: 3 key: z")        
        self.basic_test(response, '0')         
        self.separator_test(response, self.PIPE_SEPARATOR)

    def test_wiki_summary_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ Wikipedia summary: term: Mercury limit: 3 key: z")  
        self.basic_test(response, '1')         
        response = app.process_message(default_user, "@ Wikipedia summary: term: zv#432v* limit: 3 key: z") 
        self.basic_test(response, '2')         


class TestYelp(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    
    
    def test_yelp(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ yelp search : key: f longlat: false near: Durham, NC category: Mexican")
        self.basic_test(response, '0')  
        self.separator_test(response, self.PIPE_SEPARATOR)
        self.separator_test(response, self.CARROT_SEPARATOR)
        response = app.process_message(default_user, "@ yelp search : key: f near: Durham, NC category: Mexican")
        self.basic_test(response, '0')  
        self.separator_test(response, self.PIPE_SEPARATOR)
        self.separator_test(response, self.CARROT_SEPARATOR)        

    def test_yelp_geo(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ yelp search : key: f longlat: true near: 37.2530721,-121.9050031 category: chinese")
        self.basic_test(response, '0')        
        self.separator_test(response, self.PIPE_SEPARATOR)
        self.separator_test(response, self.CARROT_SEPARATOR)

    def test_yelp_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@Yelp: near: San Jose, CA category: 4230rfds key: z")
        self.basic_test(response, '1')         
        response = app.process_message(default_user, "@Yelp: near: dsjfsdjf232 category: Indian key: z")
        self.basic_test(response, '1')         

class TestMaps(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_maps(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, '@ maps directions : key: e  to: Castro Street, Mountain View, CA  from: Cambrian Park, San Jose, CA mode: driving geo: t')
        self.basic_test(response, '0') 
        self.separator_test(response, self.PIPE_SEPARATOR)
        self.separator_test(response, self.CARROT_SEPARATOR)

    def test_maps_geo(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, '@ maps directions : key: e  to: Castro Street, Mountain View, CA  from: 37.253135,-121.904945 mode: driving geo: t')
        self.basic_test(response, '0')               
        self.separator_test(response, self.PIPE_SEPARATOR)
        self.separator_test(response, self.CARROT_SEPARATOR)

    def test_maps_missing_space(self): #maps api result is missing space before the word Destination 
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ maps directions : key: b to: 2001 W Worley St, Columbia, MO 65203 from: 38.94685757,-92.39766959 mode: driving")
        self.basic_test(response, '0')               
        switch = False
        for msg in response['messages']:
            if '- Destination' in msg:
                switch = True
        self.assertTrue(switch)
        self.separator_test(response, self.PIPE_SEPARATOR)
        self.separator_test(response, self.CARROT_SEPARATOR)

    def test_maps_error(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ maps directions : key: d  to: 43@!$#!  from: fdsf13 mode: driving")
        self.basic_test(response, '1')         

class TestUnicode(BaseTest):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()    

    def test_unicode(self):
        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ wikipedia summary : key: ob term : Coursera  limit : 3")        
        self.basic_test(response, '0')               
        self.separator_test(response, self.PIPE_SEPARATOR)
        

class TestMain(BaseTest):

    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()

    def test_process_message(self):

        default_user = User.objects(phone_number="5734894023").first()
        response = app.process_message(default_user, "@ Wikipedia search: term: Ford limit: 3 key: z")
        self.basic_test(response, '0')         
        response = app.process_message(default_user, "@ Wikipedia summary: term: cars limit: 5 key: z")
        self.basic_test(response, '0')         
        response = app.process_message(default_user, "@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1")
        self.basic_test(response, '0')                  
        response = app.process_message(default_user, "@Maps directions: from: san jose, CA to: san francisco, CA key: z")
        self.basic_test(response, '0')                 
        response = app.process_message(default_user, "@Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking")

print 'Running tests in backend/tests.py ---'
if __name__ == "__main__":
    unittest.main()
