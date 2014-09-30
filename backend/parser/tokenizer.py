import re

class Tokenizer():
    def __init__(self, query="help"):
        self.tokenize(query)

    def tokenize(self, query):
        comp = re.compile(r" *:|:")
        lastPos = 0
        tokens = []
        for match in comp.finditer(query):
            pos = match.start()
            size = len(match.group())
            str = query[lastPos:pos].strip()
            #Find last index of white space. As we need to separate the key before the ":"
            if " " in str:
                key_start = str.rfind(" ")
                key = str[key_start:]
                remains = str[0:key_start]
                tokens.append(remains.strip())
                tokens.append(key.strip())
            else:
                tokens.append(str.strip())
            lastPos = pos + size
        if lastPos != len(query):
            tokens.append(query[lastPos:].strip())
        self.tokens = tokens 
        self.api = tokens[0]
        self.argument_tokens = tokens[1:]
        self.create_arguments_dict()
        return tokens

    def create_arguments_dict(self):
        arguments_dict = {}
        tokens = self.argument_tokens
        for i, token in enumerate(tokens):
            if (i % 2 == 0):
                arguments_dict[tokens[i]]= tokens[i+1]
        self.arguments_dict = arguments_dict

if __name__ == "__main__":
    t = Tokenizer("Yelp: near: Chapel Hill, NC distance: 100")
    t.tokenize("Yelp: near: Chapel Hill, NC distance: 100")
    t.tokenize("Maps: from: Chapel Hill, to: Alan")
    t.tokenize("more")

# def tokenize(query):
#     tokens = [token.strip().split() for token in query.split(":")]
#     results = [] 
#     for i, token in enumerate(tokens[:-1]):
#         key_field = tokens[i][-1]
#         value_field = tokens[i+1]
#         if (i == len(tokens)-2):
#             results.append((key_field, ' '.join(value_field)))
#         elif (i != 0):
#             results.append((key_field, ' '.join(value_field[:-1])))
#         else:
#             results.append(token[0])
#     print results 








