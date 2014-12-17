import unittest
import sys
sys.path.append('..')
import wrapper.yelp_wrapper as yelp

class TestYelp(unittest.TestCase):
    def test_yelp(self):
        """ Test Yelp Basic Functionality"""
        places = yelp.query('San Francisco, CA', 8.0, 'baseball', 7)
        self.assertNotEqual(places, None)
        self.assertTrue(len(places)>=1)

    def test_yelp_geo(self):
        """Test Yelp from Geo"""
        places = yelp.query_geo(36.00532112,-78.9260447, 8.0, 'indian', 4)
        self.assertNotEqual(places, None)
        self.assertTrue(len(places)>=1)
        

if __name__ == "__main__":
    unittest.main()
