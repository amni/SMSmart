import re

class Tokenizer():
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
        print tokens

if __name__ == "__main__":
    t = Tokenizer()
    t.tokenize("Yelp: near: Chapel Hill, NC distance: 100")
    t.tokenize("Maps: from: Chapel Hill, to: Alan")
    t.tokenize("more")







