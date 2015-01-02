from flask import Flask, request, jsonify, render_template

from mongoengine import *
from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp
from controller.maps import Maps
from controller.onboard import Onboard
from controller.attractions import Attractions
from controller.default import Default
from controller.limit import Limit
import twilio.twiml
from models import User, Query
from twilio.rest import TwilioRestClient
from controller.wikipedia import Wikipedia

import os

app = Flask(__name__)
account_sid = "AC171ca34ca45bf15bb3f369b1ae5e9a9f"
auth_token = "1d3ef112c1407035c6c6f5e5e17f75ad"
client = TwilioRestClient(account_sid, auth_token)
PHONE_NUMBERS = ["+15738182146", "+19738280148", "+16503534855", "+18704740576", "+18702802312"]
PLANS = ["Budget":50, "Pro": 100, "Premium":200]
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
    user = get_user(phone_number)
    if user.is_over_limit():
        user_text_message = "limit"
    results = process_message(user, user_text_message)
    messages_list = results.get("messages")
    key = results.get("key", "")
    user_query = Query(query_id = key)
    user_query.save()
    user.queries.append(user_query)
    user.save() 
    if not wifi_request: 
        distribute(str(phone_number), messages_list, key)
        return ""
    return jsonify(results=response_text_message)

@app.route('/upgrade', methods=["POST"])
def upgrade_account():
    try:
        account_type = request.values.get('Account')
        phone_number = request.values.get('From')
        user = get_user(phone_number)
        user.text_limit = PLANS[account_type]
        return jsonify(success=True)
    except:
        return jsonify(success=False)

def get_phone_number():
    from_number = PHONE_NUMBERS.pop(0)
    PHONE_NUMBERS.append(from_number)
    return from_number

def get_user(phone_number):
    user = User.objects(phone_number=phone_number).first()
    if not user:
        user = User(phone_number=phone_number)
        user.save()
    return user

def distribute(phone_number, messages_list, key):
    for message in messages_list:
        message = "".join([key, message])
        message.encode('utf-8', 'ignore')
        client.messages.create(to=phone_number, from_=get_phone_number(), body=message)

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
    if type == "onboard": return Onboard()
    if type == "limit": return Limit()
    assert 0, "Invalid string " + type 
    return None 

if __name__ == '__main__':
    app.run(debug=True) 