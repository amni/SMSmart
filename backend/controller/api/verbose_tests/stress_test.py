import unittest
import sys
sys.path.append('..')
import wrapper.maps_wrapper as maps
import wrapper.tripadvisor_wrapper as tripadvisor
import wrapper.yelp_wrapper as yelp

class TestAPI(unittest.TestCase):
    def test_yelp(self):
        """ Test Yelp"""
        places = yelp.query('San Francisco, CA', 8.0, 'baseball', 7)
        for restaurant in places:
            print restaurant.to_string()

    def test_yelp_geo(self):
        """Test Yelp from Geo"""
        places = yelp.query_geo(36.00532112,-78.9260447, 8.0, 'indian', 4)
        for restaurant in places:
            print restaurant.to_string()


    def test_yelp_verbose(self):
        """Test Yelp Verbose"""
        places = yelp.query('San Jose, CA', 8.0, 'indian', 6)
        for restaurant in places:
            print restaurant.to_string_verbose()        


    def test_maps_directions(self):
        """Test Maps Directions"""
        directions = maps.query('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print directions
        
    # def test_maps_get_distance(self):
    #     """Test Maps Distance"""        
    #     distance = maps.getDistance('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
    #     print distance

    def test_maps_convert_geo_location(self):
        """Test Maps Geo Location Conversion"""        
        location = maps.get_location_string(36.00532112,-78.9260447)
        print location

    # Not currently supporting trip advisor

    # def test_tripadvisor(self):
    #     """Test Tripadvisor"""
    #     places = tripadvisor.query('Durham, NC, USA')
    #     for attr in places:
    #         print attr.to_string()


    # def test_tripadvisor_geo(self):
    #     """Test Tripadvisor from Geo"""
    #     places = tripadvisor.query_geo(37.253, -121.90)
    #     for restaurant in places:   
    #         print restaurant.to_string()

    # def test_tripadvisor_verbose(self):
    #     """Test Tripadvisor Verbose"""
    #     places = tripadvisor.query('Durham, NC, USA')
    #     for restaurant in places:
    #         print restaurant.to_string_verbose()        

if __name__ == "__main__":
    unittest.main()
