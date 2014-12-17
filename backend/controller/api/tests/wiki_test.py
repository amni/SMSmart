import unittest
import sys
sys.path.append('..')
import wrapper.wikipedia_wrapper as wiki


class TestWikipedia(unittest.TestCase):
    def test_wiki_summary(self):
        """Wikipedia Summary"""
        terms = {"Barack Obama":1, "Barack Obama":3, "Coursera":3, "Pune, India":3, "ISIS":3, "Ford":5}
        for key, value in terms.iteritems():
            result = wiki.summary(key, value)
            self.assertNotEqual(result, None)

    def test_wiki_search(self):
        """Wikipedia Search"""
        terms = {'ball':3, 'John McCain':2, 'Pinterest':3, 'Uber':5, 'taxi':10}
        for key, value in terms.iteritems():
            result = wiki.search(key, value)
            self.assertNotEqual(result, None)

if __name__ == "__main__":
    unittest.main()

