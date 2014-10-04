import sys
sys.path.append('..')

import yelp.wrapper

def test_yelp():
	places = yelp.wrapper.query('San Jose, CA', 8.0, 'indian')
	for restaurant in places:
		print restaurant.to_string()
	print

def test_yelp_verbose():
	places = yelp.wrapper.query('San Jose, CA', 8.0, 'indian')
	for restaurant in places:
		print restaurant.to_string_verbose()		
	print


test_yelp()
test_yelp_verbose()