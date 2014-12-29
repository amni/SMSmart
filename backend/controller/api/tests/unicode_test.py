import unittest
import sys
sys.path.append('..')
import wrapper.yelp_wrapper as yelp


class TestUnicode(unittest.TestCase):
    def test_yelp(self):
        """ Yelp Unicode Test """
        places = yelp.query('San Francisco, CA', 5.0, 'restaurants', 20)
        self.assertNotEqual(places, None)
    
print 'Running tests in backend/controller/api/tests/unicode_test.py ---'

if __name__ == "__main__":
    unittest.main()

