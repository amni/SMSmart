from flask import Flask, request

from mongoengine import *
from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp
from controller.maps import Maps
from controller.attractions import Attractions
from controller.default import Default
import twilio.twiml
from models import User, Variable

import os

app = Flask(__name__)

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
    	user.last_query_response = response_text_message
    	user.save()
    resp = send_text(response_text_message)
    return str(resp)

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