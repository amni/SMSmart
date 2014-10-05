
import app
import unittest
from models import User, Variable


class TestParser(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)
        new_user = User(phone_number="5734894023")
        new_user.save()

    def test_process_message(self):
        """Checks that that modules are loading correctly"""
        default_user = User.objects(phone_number="5734894023").first()
        print app.process_message(default_user, "yelp: near: Times Square, New York")
        print app.process_message(default_user, "yelp help")
        print app.process_message(default_user, "yelp info: place: 1")
        print app.process_message(default_user, "Yelp: near: Durham, NC category: bars")
        print app.process_message(default_user, "yelp info: place: 1")
        print app.process_message(default_user, "Yelp search: near: chapel hill, NC distance: 5")
        print app.process_message(default_user, "maps directions: from: chapel hill, NC to: Durham, NC")





    def test_parse_module(self):
        """Checks that the parser parses the first word correctly"""
        pass

    
if __name__ == "__main__":
    unittest.main()
