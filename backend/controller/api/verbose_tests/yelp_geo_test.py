import unittest
import sys
sys.path.append('..')
import wrapper.yelp_wrapper as yelp


class TestYelpGeo(unittest.TestCase):
    def test_yelp_geo(self):
        """Tests Yelp Geo"""
        places = yelp.query_geo(36.0053107,-78.9263559, 8.0, 'indian', 4)
        for restaurant in places:
            print restaurant.to_string()

    def test_yelp(self):
        """Tests Yelp Query"""
        places = yelp.query('San Francisco,CA', 8.0, 'baseball', 7)
        for restaurant in places:
            print restaurant.to_string()

if __name__ == "__main__":
    unittest.main()

