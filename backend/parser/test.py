__author__ = 'Ben'

import tokenizer

def test():
    token = tokenizer.Tokenizer()
    print token.tokenize("Yelp: test case")
