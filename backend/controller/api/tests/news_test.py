import unittest
import sys
sys.path.append('..')
import wrapper.news_wrapper as news

class TestNews(unittest.TestCase):
    def test_news_feed(self):
        """Test News Feed"""    
        response = news.get_tweets()
        self.assertNotEqual(response, None)
        self.assertTrue(len(response)>=1)

    def test_news_feed_invalid_user(self):
        """Test News Feed"""    
        response = news.get_tweets("432feds")
        self.assertEqual(response, 1)

    def test_news_feed_with_handle(self):
        """Test News Feed"""    
        response = news.get_tweets("ESPN_FirstTake")
        self.assertNotEqual(response, None)
        self.assertTrue(len(response)>=1)

print 'Running tests in backend/controller/api/tests/news_test.py ---'
 
if __name__ == "__main__":
    unittest.main()

