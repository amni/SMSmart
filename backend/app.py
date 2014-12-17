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
SMS_LENGTH = 160
MSG_SEGMENT_LENGTH = 150
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
    response_text_message = process_message(user, user_text_message)
    output = response_text_message
    key_position = output.find('^')
    key = output[:key_position]
    user_query = Query(query_id = key, response = response_text_message)
    user_query.save()
    user.queries.append(user_query)
    user.save() 
    if not wifi_request: 
        messages_list = split_into_messages(output)
        distribute(str(phone_number), messages_list)
    return jsonify(results=response_text_message)

def get_phone_number():
    from_number = numbers.pop(0)
    numbers.append(from_number)
    return from_number

def split_into_messages(output):
    messages_list = []
    key_position = output.find('^')
    key = output[:key_position]
    output = output[key_position+1:]
    position = 0
    remainder = len(output)
    msg_number = 1
    temp = remainder/MSG_SEGMENT_LENGTH
    total_msg = temp + 1 if (remainder%MSG_SEGMENT_LENGTH != 0) else temp
    while remainder > MSG_SEGMENT_LENGTH: 
        message = output[position:position+MSG_SEGMENT_LENGTH]
        metadata = key + '(' + str(msg_number) + '/' + str(total_msg) + ')' + '*'
        msg_number += 1        
        remainder -= MSG_SEGMENT_LENGTH
        position += MSG_SEGMENT_LENGTH
        messages_list.append(metadata+message)
    if remainder > 0:
        message = output[position:]
        metadata = key + '(' + str(msg_number) + '/' + str(total_msg) + ')' + '*'
        msg_number += 1   
        messages_list.append(metadata+message)
    return messages_list

def distribute(phone_number, messages_list):
    for message in messages_list:
        client.messages.create(to=phone_number, from_=get_phone_number(), body=message)

def send_text(message):
    resp = twilio.twiml.Response()
    resp.message(message)
    return resp

def process_message(user, user_text_message):
    tokenizer = Tokenizer(user_text_message)
    api = create_subprogram(tokenizer.api)
    result = (getattr(api, tokenizer.program)(user, **tokenizer.arguments_dict)).encode('utf-8', 'ignore')
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