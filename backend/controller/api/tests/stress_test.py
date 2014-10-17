import unittest
import sys
sys.path.append('..')
import travel.maps_wrapper as maps
import travel.tripadvisor_wrapper as tripadvisor
import travel.yelp_wrapper as yelp

class TestAPI(unittest.TestCase):
    def test_yelp(self):
        print '--- Test Yelp ---'
        places = yelp.query('San Francisco, CA', 8.0, 'baseball', 7)
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'

    def test_yelp_geo(self):
        print '--- Test Yelp from Geo ---'
        places = yelp.query_geo(36.00532112,-78.9260447, 8.0, 'indian', 4)
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'


    def test_yelp_verbose(self):
        print '--- Test Yelp Verbose ---'
        places = yelp.query('San Jose, CA', 8.0, 'indian', 6)
        for restaurant in places:
            print restaurant.to_string_verbose()        
        print ' ----------------'


    def test_maps_directions(self):
        print '--- Test Maps Directions ---'
        directions = maps.query('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print directions
        print ' ----------------'
        
    def test_maps_get_distance(self):
        print '--- Test Maps Distance ---'        
        distance = maps.getDistance('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print distance
        print ' ----------------'

    def test_maps_convert_geo_location(self):
        print '--- Test Maps Geo Location Conversion ---'        
        location = maps.get_location_string(36.00532112,-78.9260447)
        print location
        print ' ----------------'        

    def test_tripadvisor(self):
        print '--- Test Tripadvisor ---'
        places = tripadvisor.query('Durham, NC, USA')
        for attr in places:
            print attr.to_string()
        print ' ----------------'


    def test_tripadvisor_geo(self):
        print '--- Test Tripadvisor from Geo ---'
        places = tripadvisor.query_geo(37.253, -121.90)
        for restaurant in places:
            print restaurant.to_string()
        print ' ----------------'

    def test_tripadvisor_verbose(self):
        print '--- Test Tripadvisor Verbose ---'
        places = tripadvisor.query('Durham, NC, USA')
        for restaurant in places:
            print restaurant.to_string_verbose()        
        print ' ----------------' 

if __name__ == "__main__":
    unittest.main()
