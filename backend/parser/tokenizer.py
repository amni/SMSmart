import re

class Tokenizer():
    def __init__(self, query="help"):
        self.tokenize(query)

    def tokenize(self, query):
        tokens = [token.strip().split() for token in query.split(":")]
        results = {}
        for i, token in enumerate(tokens[:-1]):
            key_field = tokens[i][-1]
            value_field = tokens[i+1]
            if (i == 0):
                continue
            if (i == len(tokens)-2):
                results[key_field] = ' '.join(value_field)
            elif (i != 0):
                results[key_field] = ' '.join(value_field[:-1])

        self.tokens = tokens
        self.api = tokens[0][0]
        if(len(tokens[0])>1):
            self.program = tokens[0][1]
        else:
            self.program = 'default'

        self.arguments_dict = results

if __name__ == "__main__":
    t = Tokenizer("Yelp: near: Chapel Hill, NC distance: 100")
    tokens = t.tokenize("Yelp: near: Chapel Hill, NC distance: 100")
    print t.arguments_dict, t.api, t.program
    # t.tokenize("Maps: from: Chapel Hill, to: Alan")
    # print t.arguments_dict
    # t.tokenize("more")
    # print t.arguments_dict







