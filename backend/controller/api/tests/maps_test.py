import unittest
import sys
sys.path.append('..')
import wrapper.maps_wrapper as maps

class TestMaps(unittest.TestCase):
    def test_maps_get_distance(self):
        """Test Maps Distance"""    
        distance = maps.get_distance('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        self.assertEqual(distance, '9.2 mi')

    def test_maps_directions(self):
        """Test Maps Directions"""
        directions = maps.query('Duke University, Durham, NC', 'UNC Chapel Hill, Chapel Hill, NC')
        self.assertNotEqual(directions, None)
        self.assertTrue(len(directions)>=1)   

    def test_maps_convert_geo_location(self):
        """Test Maps Geo Location Conversion"""        
        location = maps.get_location_string(36.00532112,-78.9260447)
        durham_location = "Durham, NC 27705"
        self.assertTrue(durham_location in location)


if __name__ == "__main__":
    unittest.main()

