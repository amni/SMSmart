
from models import parser 
import unittest



class TestParser(unittest.TestCase):
	def setup(self):
		self.parser = SMSParser()

	def test_config_loading(self):
		"""Checks that that modules are loading correctly"""
		keyword_dict = self.parser.keyword_dict 
		self.assertTrue(len(keyword_dict["yelp"]["keys"])> 0 ) 




	def test_parse_module(self):
		"""Checks that the parser parses the first word correctly"""
		self.assertEqual(self.parser.parse_module("yelp restaurants near chapel hill"), "yelp")
		self.assertEqual(self.parser.parse_module("maps directions from chapel hill to durham"), "maps")
		self.assertEqual(self.parser.parse_module("tripad attractions in paris"), "tripad")

	
if __name__ == "__main__":
	unittest.main()
