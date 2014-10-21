import unittest
import sys
sys.path.append('..')
import travel.tripadvisor_wrapper as tripadvisor


class TestNoneTypeTripAdvisor(unittest.TestCase):
    def test_tripadvisor_verbose(self):
        print '--- Test Tripadvisor Verbose ---'
        places = tripadvisor.query('Durham, NC, USA')
        for attr in places:
            print attr.to_string_verbose()        
        print ' ----------------' 
    

if __name__ == "__main__":
    unittest.main()

