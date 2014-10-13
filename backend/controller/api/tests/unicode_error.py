import unittest
import sys
sys.path.append('..')
import yelp.wrapper
import maps.wrapper
import tripadvisor.wrapper

class TestUnicode(unittest.TestCase):
    def test_yelp(self):
        print '--- Test Yelp ---'
        places = yelp.wrapper.query('Tribeca, New York City, NY')
        if places is None:
        	print 'HTTP Error: Couldn\'t handle'
        	return 
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'


if __name__ == "__main__":
    unittest.main()
