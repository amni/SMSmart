from flask import Flask, request

from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def receive_message():
    user_text_message = request.values.get('Body')
    phone_number = request.values.get('From')
    print 'hits here'
    response_text_message = "test"
    resp = twilio.twiml.Response()
    resp.message(response_text_message)
    return str(resp)

def process_message(user_text_message):
	#Send it to the parser
	tokenizer = Tokenizer(user_text_message)
	api = create_subprogram(tokenizer.api)
	return api.find_results(**tokenizer.arguments_dict)

def create_subprogram(type):
	if type == "yelp": return Yelp() 
	if type == "maps": return Maps()
	assert 0, "Invalid string " + type 
	return None 

if __name__ == '__main__':
    app.run(debug=True)