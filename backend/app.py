from flask import Flask, request

from mongoengine import *
from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp
from controller.maps import Maps
from controller.attractions import Attractions
from controller.default import Default
import twilio.twiml
from models import User, Variable
from twilio.rest import TwilioRestClient

import os

app = Flask(__name__)
account_sid = "AC171ca34ca45bf15bb3f369b1ae5e9a9f"
auth_token = "1d3ef112c1407035c6c6f5e5e17f75ad"
client = TwilioRestClient(account_sid, auth_token)
numbers = ["+15738182146", "+19738280148"]

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
    user = User.objects(phone_number=phone_number).first()
    if not user:
    	response_text_message = get_onboard_message()
    	user = User(phone_number=phone_number)
    	user.save()
    else: 
    	response_text_message = process_message(user, user_text_message)
    resp = send_text(response_text_message)
    distribute(str(phone_number), str(response_text_message))
    return ''

def distribute(phone_number, output):
    position = 0
    remainder = len(output)
    while remainder > 160:
        message = output[position:position+157]
        remainder -= 157
        position += 157
        from_number = numbers.pop(0)
        numbers.append(from_number)
        client.messages.create(to=phone_number, from_=from_number, body=message)
    if remainder > 0:
        message = output[position:]
        from_number = numbers.pop(0)
        numbers.append(from_number)
        client.messages.create(to=phone_number, from_=from_number, body=message)

def send_text(message):
	resp = twilio.twiml.Response()
	resp.message(message)
	return resp

def process_message(user, user_text_message):
	tokenizer = Tokenizer(user_text_message)
	api = create_subprogram(tokenizer.api)
	return getattr(api, tokenizer.program)(user, **tokenizer.arguments_dict)

def get_onboard_message():
	return """
	Welcome to SMSMart\n
	You can look up restaurants, get directions, or find attractions here!\n
	To try it out text us back with yelp help, maps help, or trip help
	"""

def create_subprogram(type):
	if type == "yelp": return Yelp() 
	if type == "maps": return Maps()
	if type == "attractions": return Attractions()
	assert 0, "Invalid string " + type 
	return None 

if __name__ == '__main__':
	app.run(debug=True) 