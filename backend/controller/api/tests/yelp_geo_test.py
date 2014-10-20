import unittest
import sys
sys.path.append('..')
import travel.yelp_wrapper as yelp


class TestYelpGeo(unittest.TestCase):
    def test_yelp_geo(self):
        print '--- Test Yelp from Geo ---'
        places = yelp.query_geo(36.0053107,-78.9263559, 8.0, 'indian', 4)
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'

    def test_yelp(self):
        print '--- Test Yelp ---'
        places = yelp.query('San Francisco,CA', 8.0, 'baseball', 7)
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'  

if __name__ == "__main__":
    unittest.main()

