import unittest
import sys
sys.path.append('..')
import travel.yelp_wrapper as yelp


class TestUnicode(unittest.TestCase):
    def test_yelp(self):
        print '--- Test Yelp ---'
        places = yelp.query('San Francisco, CA', 5.0, 'restaurants', 20)
        if places is None:
        	print 'HTTP Error: Couldn\'t handle'
        	return 
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'
    

if __name__ == "__main__":
    unittest.main()

