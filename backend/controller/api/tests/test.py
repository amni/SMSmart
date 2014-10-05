import unittest
import sys
sys.path.append('..')
import yelp.wrapper
#import tripadvisor.wrapper
import maps.maps

class TestParser(unittest.TestCase):
	def test_yelp(self):
		places = yelp.wrapper.query('San Jose, CA', 8.0, 'indian')
		for restaurant in places:
			print restaurant.to_string()
		print

	def test_yelp_verbose(self):
		places = yelp.wrapper.query('San Jose, CA', 8.0, 'indian')
		for restaurant in places:
			print restaurant.to_string_verbose()		
		print

if __name__ == "__main__":
    unittest.main()
