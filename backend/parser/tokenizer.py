import re
import os
from mongoengine import *
from models import User, Query, Text, TextPart

if 'PORT' in os.environ: 
    import re
    from mongoengine import connect

    regex = re.compile(r'^mongodb\:\/\/(?P<username>[_\w]+):(?P<password>[\w]+)@(?P<host>[\.\w]+):(?P<port>\d+)/(?P<database>[_\w]+)$')

    # grab the MONGOLAB_URI
    mongolab_url = os.environ['MONGOLAB_URI']

    # get our match
    match = regex.search(mongolab_url)
    data = match.groupdict()

    # now connect
    connect(data['database'], host=data['host'], port=int(data['port']), username=data['username'], password=data['password'])

    # import logging
    # from logging import StreamHandler
    # file_handler = StreamHandler()
    # app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
    # app.logger.addHandler(file_handler)

else:
    # not heroku (dev env)
    # connect to mongo
    connect('smsmart')

class Tokenizer():
    def __init__(self, query = "@news feed: key:7"):
        self.partial_text = False
        self.tokenize(query)

    def tokenize(self, query):
        self.format = "default"
        if query[0] == "@":
            self.tokenize_default(query)
        else: 
            key = self.extract_key(query)
            text = Text.objects(key = key).first()
            if not text:
                text = self.store_text(query, key) 
                text.text_parts.append(self.store_text_part(query))
                text.save()
                self.partial_text = True 
            else:
                text.text_parts.append(self.store_text_part(query))
                text.save()
                if text.total_expected == len(text.text_parts):
                    self.extract_tokens(self.form_text(text))
                else:
                    self.partial_text = True 



    def tokenize_default(self, query):
        self.format = "android"
        query = query[1:]
        self.extract_tokens(query)

    def extract_tokens(self, query):
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

    def extract_key(self, query):
        key_end = query.find("(")
        return query[:key_end]

    def store_text(self, query, key):
        text = Text(key = key, total_expected = self.get_num_texts_expected(query))
        text.save()
        return text

    def store_text_part(self, query):
        text_part = TextPart(content = self.extract_text(query), 
                                num = self.get_part_num(query))
        text_part.save()
        return text_part

    def get_part_num(self, query):
        key_end = query.find("(")
        slash_location = query.find("/")
        return int(query[key_end+1:slash_location])

    def get_num_texts_expected(self, query):
        slash_location = query.find("/")
        parentheses_end = query.find(")")
        return int(query[slash_location+1:parentheses_end])

    def extract_text(self, query):
        parentheses_end = query.find(")")
        return query[parentheses_end+1:]

    def form_text(self, text):
        query = ""
        for part in sorted(text.text_parts, key = lambda x : x.num):
            query+= part.content 
        return query[1:]
