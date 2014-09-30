
import app
import unittest



class TestParser(unittest.TestCase):
    def setup(self):
        self.app = app.test_client(use_cookies=True)

    def test_process_message(self):
        """Checks that that modules are loading correctly"""
        print app.process_message("yelp: near: chapel hill, NC distance: 5")




    def test_parse_module(self):
        """Checks that the parser parses the first word correctly"""
        pass

    
if __name__ == "__main__":
    unittest.main()
