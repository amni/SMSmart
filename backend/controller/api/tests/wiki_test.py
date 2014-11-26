import unittest
import sys
sys.path.append('..')
import info.wikipedia_wrapper as wiki


class TestWikipedia(unittest.TestCase):
    def test_wiki_summary(self):
        terms = {"Barack Obama":1, "Barack Obama":3, "Coursera":3, "Pune, India":3, "ISIS":3}
        counter = 0
        print 
        for key, value in terms.iteritems():
            counter += 1 
            print "Test " + str(counter) + ": " + key + ", " + str(value)
            result = wiki.summary(key, value)
            print result 
            print len(result)

    def test_wiki_search(self):
        terms = {'ball':3, 'John McCain':2, 'Pinterest':3, 'Uber':5, 'taxi':10}
        counter = 0
        print 
        for key, value in terms.iteritems():
            counter += 1 
            print "Test " + str(counter) + ": " + key + ", " + str(value)
            result = wiki.search(key, value)
            print result 


if __name__ == "__main__":
    unittest.main()

