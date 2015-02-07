import re
from models import User, Query

class Tokenizer():
    def __init__(self, query="help"):
        self.tokenize(query)

    def tokenize(self, query):
        self.format = "default"
        if query[0] == "@":
            self.format = "android"
            query = query[1:]
        tokens = [token.strip().split() for token in query.split(":")]
        results = {}
        for i, token in enumerate(tokens[:-1]):
            key_field = tokens[i][-1].lower()
            value_field = tokens[i+1]
            if (i == 0):
                continue
            if (i == len(tokens)-2):
                results[key_field] = ' '.join(value_field)
            elif (i != 0):
                results[key_field] = ' '.join(value_field[:-1])
        self.tokens = tokens
        self.api = tokens[0][0].lower()
        if(len(tokens[0])>1):
            self.program = tokens[0][1]
        else:
            self.program = "default"
        self.arguments_dict = results
        self.arguments_dict["format"] = self.format

    def replace_variables(self, query):
        pass

if __name__ == "__main__":
    pass
