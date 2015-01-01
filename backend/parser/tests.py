import unittest
import tokenizer 


class BaseTest(unittest.TestCase):
    def check_arguments(self, arguments_dict, arguments_list):
        for term in arguments_list:
            self.assertTrue(term in arguments_dict)

class TestTokenizer(BaseTest):
    def test_format(self):        
        response = tokenizer.Tokenizer('@ Wikipedia summary: term: Ford limit: 3 key: z')
        self.assertEquals(response.format, 'android')
        response = tokenizer.Tokenizer('Wikipedia summary: term: Ford limit: 3 key: z')
        self.assertEquals(response.format, 'default')

    def test_api(self):
        response = tokenizer.Tokenizer('@ Wikipedia summary: term: Ford limit: 3 key: z')
        self.assertEquals(response.api, 'wikipedia')        
        response = tokenizer.Tokenizer('@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1')
        self.assertEquals(response.api, 'yelp')        
        response = tokenizer.Tokenizer('@ Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking')
        self.assertEquals(response.api, 'maps')

    def test_program(self):
        response = tokenizer.Tokenizer('@ Wikipedia : term: Ford limit: 3 key: z')
        self.assertEquals(response.program, 'default')        
        response = tokenizer.Tokenizer('@ Wikipedia summary: term: Ford limit: 3 key: z')
        self.assertEquals(response.program, 'summary')                
        response = tokenizer.Tokenizer('@ Wikipedia search: term: Ford limit: 3 key: z')
        self.assertEquals(response.program, 'search')        
        response = tokenizer.Tokenizer('@ Maps directions: from: chapel hill, NC to: Durham, NC key: z mode: walking')
        self.assertEquals(response.program, 'directions')                
        response = tokenizer.Tokenizer('@ Maps 342dfs: from: chapel hill, NC to: Durham, NC key: z mode: walking')
        self.assertEquals(response.program, '342dfs')        

    def test_arguments_dict(self):
        response = tokenizer.Tokenizer('@ Wikipedia : term: Ford limit: 3 key: z')
        self.assertEquals(len(response.arguments_dict), 4)        
        self.check_arguments(response.arguments_dict, ['term', 'limit', 'key'])
        response = tokenizer.Tokenizer('@Yelp search:  longlat: true near: 40.74503998,-73.99879607 category: Pizza key: z limit: 1')
        self.assertEquals(len(response.arguments_dict), 6)        
        self.check_arguments(response.arguments_dict, ['longlat', 'near', 'category', 'key', 'limit'])
        response = tokenizer.Tokenizer('@ yelp search : key: f near: Durham, NC category: Mexican')
        self.assertEquals(len(response.arguments_dict), 4)        
        self.check_arguments(response.arguments_dict, ['near', 'category', 'key'])

print 'Running tests in backend/parser/tests.py ---'

if __name__ == "__main__":
    unittest.main()