import unittest
import sys
sys.path.append('..')
import yelp.wrapper
import maps.wrapper
#import tripadvisor.wrapper

class TestAPI(unittest.TestCase):
    def test_yelp(self):
        print '--- Test Yelp ---'
        places = yelp.wrapper.query('San Jose, CA', 8.0, 'baseball')
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'

    def test_yelp_geo(self):
        print '--- Test Yelp from Geo ---'
        places = yelp.wrapper.query_geo(37.253, -121.90, 8.0, 'indian')
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'

    def test_yelp_verbose(self):
        print '--- Test Yelp Verbose ---'
        places = yelp.wrapper.query('San Jose, CA', 8.0, 'indian')
        for restaurant in places:
            print restaurant.to_string_verbose()        
        print ' ----------------'

    def test_maps_directions(self):
        print '--- Test Maps Directions ---'
        directions = maps.wrapper.query('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print directions
        print ' ----------------'

    def test_maps_get_distance(self):
        print '--- Test Maps Distance ---'        
        distance = maps.wrapper.getDistance('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print distance
        print ' ----------------'

    def test_maps_convert_geo_location(self):
        print '--- Test Maps Geo Location Conversion ---'        
        location = maps.wrapper.get_location_string(37.253,-121.90)
        print location
        print ' ----------------'        

if __name__ == "__main__":
    unittest.main()
