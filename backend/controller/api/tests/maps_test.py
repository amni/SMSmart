import unittest
import sys
sys.path.append('..')
import travel.maps_wrapper as maps

class TestMaps(unittest.TestCase):
    def test_maps_directions(self):
        print '--- Test Maps Directions ---'
        directions = maps.query('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print directions
        print ' ----------------'
        
    def test_maps_get_distance(self):
        print '--- Test Maps Distance ---'        
        distance = maps.get_distance('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        print distance
        print ' ----------------'

    def test_maps_convert_geo_location(self):
        print '--- Test Maps Geo Location Conversion ---'        
        location = maps.get_location_string(36.00532112,-78.9260447)
        print location
        print ' ----------------'      


if __name__ == "__main__":
    unittest.main()

