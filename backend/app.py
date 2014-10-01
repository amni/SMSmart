from flask import Flask, request

from mongoengine import *
from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp
import twilio.twiml



app = Flask(__name__)
# connect('smsmart')


@app.route('/', methods=["GET", "POST"])
def receive_message():
    user_text_message = request.values.get('Body')
    phone_number = request.values.get('From')
    # TODO: check to see if it exists, if not create a new user with this phone number 
    response_text_message = process_message(user_text_message)
    resp = twilio.twiml.Response()
    resp.message(response_text_message)
    return str(resp)

def process_message(user_text_message):
	tokenizer = Tokenizer(user_text_message)
	api = create_subprogram(tokenizer.api)
	return getattr(api, tokenizer.program )(**tokenizer.arguments_dict)

def create_subprogram(type):
	if type == "yelp": return Yelp() 
	if type == "maps": return Maps()
	assert 0, "Invalid string " + type 
	return None 

if __name__ == '__main__':
    app.run(debug=True)