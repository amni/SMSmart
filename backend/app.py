from flask import Flask, request, jsonify, render_template

from mongoengine import *
from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp
from controller.maps import Maps
from controller.attractions import Attractions
from controller.default import Default
import twilio.twiml
from models import User, Query
from twilio.rest import TwilioRestClient
from controller.wikipedia import Wikipedia

import os

app = Flask(__name__)
account_sid = "AC171ca34ca45bf15bb3f369b1ae5e9a9f"
auth_token = "1d3ef112c1407035c6c6f5e5e17f75ad"
client = TwilioRestClient(account_sid, auth_token)
numbers = ["+15738182146", "+19738280148", "+16503534855", "+18704740576", "+18702802312"]
MSG_SEGMENT_LENGTH = 150
multi_message_inputs = {}
SINGLE_TEXT_MATCH = '(1/1)'

#for heroku
if 'PORT' in os.environ: 
    print os.environ
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

    import logging
    from logging import StreamHandler
    file_handler = StreamHandler()
    app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
    app.logger.addHandler(file_handler)

else:
    # not heroku (dev env)
    # connect to mongo
    connect('smsmart')

@app.route('/', methods=["GET", "POST"])
def receive_message():
    user_text_message = request.values.get('Body')
    phone_number = request.values.get('From')
    wifi_request = 'Wifi' in request.values
    user = User.objects(phone_number=phone_number).first()
    if not user:
        user = User(phone_number=phone_number)
        user.save()    
    if wifi_request:
        return jsonify(results=user_text_message)

    if single_text(user_text_message):
        start_pos = user_text_message.find(')')
        handle(user, user_text_message[start_pos+1:], phone_number)
    else:
        save(user, phone_number, user_text_message)
    return ""

def get_phone_number():
    from_number = numbers.pop(0)
    numbers.append(from_number)
    return from_number

def single_text(user_text_message):
    start_position = user_text_message.find('(')
    end_position = user_text_message.find(')')
    header = user_text_message[start_position:end_position+1]
    compare = "".join(header.split())
    if (compare == SINGLE_TEXT_MATCH):
        return True
    else:
        return False

def save(user, phone_number, user_text_message):
    delimiter_position = user_text_message.find('(')
    message_key = user_text_message[:delimiter_position]
    key = message_key+phone_number
    start_num_messages = user_text_message.find('/')
    end_num_messages = user_text_message.find(')')
    num_messages = user_text_message[start_num_messages+1:end_num_messages]
    messages = list()
    if key in multi_message_inputs:
        messages = multi_message_inputs[key]
        messages.append(user_text_message)
        multi_message_inputs[key] = messages
    else:
        messages.append(user_text_message)
        multi_message_inputs[key] = messages
    if len(messages) == int(num_messages):
        handle(user, construct_message(messages), phone_number)
        del multi_message_inputs[key]

def construct_message(messages):
    sorted_messages = {}
    for msg in messages:
        index = int(msg[msg.find('(')+1:msg.find('/')])
        sorted_messages[index] = msg[msg.find(')')+1:]
    output = ''
    for key in sorted(sorted_messages):
        output += sorted_messages[key]
    return output

def handle(user, user_text_message, phone_number):
    results = process_message(user, user_text_message)
    messages_list = results.get("messages")
    key = results.get("key", "")
    user_query = Query(query_id = key, response = user_text_message)
    user_query.save()
    user.queries.append(user_query)
    user.save() 
    distribute(str(phone_number), messages_list, key)

def distribute(phone_number, messages_list, key):
    for message in messages_list:
        message = "".join([key, message])
        message.encode('utf-8', 'ignore')
        client.messages.create(to=phone_number, from_=get_phone_number(), body=message)

def send_text(message):
    resp = twilio.twiml.Response()
    resp.message(message)
    return resp

def process_message(user, user_text_message):
    tokenizer = Tokenizer(user_text_message)
    api = create_subprogram(tokenizer.api)
    result = getattr(api, tokenizer.program)(user, **tokenizer.arguments_dict)
    return result
    
def create_subprogram(type):
    if type == "yelp": return Yelp() 
    if type == "maps": return Maps()
    if type == "wikipedia": return Wikipedia()
    if type == "attractions": return Attractions()
    assert 0, "Invalid string " + type 
    return None 

if __name__ == '__main__':
    app.run(debug=True) 