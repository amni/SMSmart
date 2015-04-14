from flask import Flask, request, jsonify, render_template

from mongoengine import *
from parser.tokenizer import Tokenizer 
from controller.yelp import Yelp
from controller.maps import Maps
from controller.onboard import Onboard
from controller.attractions import Attractions
from controller.default import Default
from controller.limit import Limit
from controller.news import News
from controller.search import Search
from controller.weather import Weather
from controller.stock import Stock
from controller.feedback import Feedback
from controller.twitter import Twitter
from controller.more import More 
from models import User, Query, Referral, Auth
from controller.wikipedia import Wikipedia
import phonenumbers 
from util import PhoneNumbersUtil
import plivo, plivoxml
import os
import datetime

app = Flask(__name__)
android_key = "bT7KZhQZUQ"
signups_open = True
PLANS = {"Free": 30, "Budget":50, "Pro": 100, "Premium":200, "Unlimited": 10000}
auth_id = "MAMJHJZDHJYZBJNJM1MZ"
auth_token = "ODMxYTkzOWRhZmQ0ODZkZmQyYzQyNjAzMmU0NmE2"
p = plivo.RestAPI(auth_id, auth_token)
phone_util = PhoneNumbersUtil()


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
    user_text_message = request.values.get('Text')
    phone_number = '+' + request.values.get('From')
    wifi_request = 'Wifi' in request.values
    user = get_user(phone_number)
    user_query = Query()
    user_query.save()
    tokenizer = Tokenizer(user_text_message)
    if tokenizer.partial_text:
        return ""
    arguments = tokenizer.arguments_dict
    if 'c' in arguments:
        country_tag = arguments["c"]      
    else:
        country_tag = 'US'
    if 'v' in arguments:
        version_number = int(arguments["v"])
    else:
        version_number = 10000
    should_rotate = False
    if tokenizer.api != "onboard" and version_number > 6:
        should_rotate = True
    results = process_message(user, user_text_message, tokenizer)
    key = results.get("key", "")
    # if user.is_over_limit():
    #     user_text_message = "limit default: key: %s" % key[1:]
    #     results = process_message(user, user_text_message, user_query)
    #     key = results.get("key" "")
    messages_list = results.get("messages")
    user_query.response = messages_list[0] if len(messages_list) else "Feedback"
    user_query.save()
    user.queries.append(user_query)
    user.save() 
    if not wifi_request: 
        distribute(str(phone_number), messages_list, key, country_tag, should_rotate)
        return ""
    return jsonify(results=prepend_key(messages_list, key))

@app.route('/upgrade', methods=["POST"])
def upgrade_account():
    try:
        text_increase = request.values.get('Texts')
        phone_number = request.values.get('From')[-10:]
        key = request.values.get('Key')
        user = get_user(phone_number)
        user.text_limit += text_increase
        user.save()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/signup', methods=["POST"])
def add_user():
    email = request.values.get('Email')
    phone_number = request.values.get('From')[-10:]
    key = request.values.get('Key')
    if key == android_key and signups_open:
        user = User.objects(phone_number=str(phone_number)).first()
        if not user: 
            user = User(phone_number = str(phone_number), email = email)
            user.save()
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/share', methods=["POST"])
def share_to_friends():
    phone_numbers = request.values.get('Nums')
    referrer = request.values.get('From')
    user = User.objects(phone_number = str(referrer)[-10:]).first()
    time = request.values.get('Timestamp')
    for phone_number in phone_numbers:
        referral = Referral(phone_number = str(phone_number)[-10:], date_referred = datetime.datetime.fromtimestamp(time/1000.0))
        referral.save()
        user.referrals.append(referral)
    user.save()
    return jsonify(success = True)

@app.route('/sharestatus', methods=["GET"])
def check_referral():
    phone_number = request.values.get('From')[-10:]
    key = request.values.get('Key')
    user = User.objects(phone_number=str(phone_number)).first()
    status = [{"num":referral.phone_number, "complete":referral.check_legal_referral()} for referral in user.referrals]
    return jsonify(status = status, success = True)


@app.route('/auth', methods=["POST"])
def add_tokens(): 
    phone_number = request.values.get('From')[-10:]
    user = User.objects(phone_number=str(phone_number)).first()
    api = request.values.get('API')
    secret = request.values.get('Secret')
    access = request.values.get('Access')
    auth = Auth(api = api, secret = secret, access = access)
    auth.save()
    user.auths.append(auth)
    user.save()
    return jsonify(success = True)


def get_user(phone_number):
    user = User.objects(phone_number=str(phone_number)[-10:]).first()
    if not user:
        new_user = User(phone_number=str(phone_number)[-10:])
        new_user.save()
        return new_user
    return user

def prepend_key(messages_list, key):
    return ["".join([key, message]).encode('utf-8', 'ignore') for message in messages_list]

def distribute(phone_number, messages_list, key, country_tag ='US', should_rotate = False):
    for message in messages_list:
        if should_rotate:
            message = rotate_text(message)
        message = "".join([key, message])
        message = remove_non_ascii(message)
        message.encode('utf-8', 'ignore')
        params = {
            'src': phone_util.get_phone_number(country_tag), 
            'dst' : phone_number, 
            'text' : message
        }
        p.send_message(params)

def rotate_text(message):
    """rotates text by 13 characters"""
    result_str = ""
    for letter in message:
        if letter.isalpha():
            int_val = ord(letter) 
            starting_val = ord('a')
            if letter.isupper():
                starting_val = ord('A')
            index_val = (int_val - starting_val + 13) % 26 + starting_val
            result_str+=str(unichr(index_val))
        elif letter == "+": 
            result_str+=" "
        elif letter == " ":
            result_str+= "+"
        else:
            result_str+=letter
    return result_str

def remove_non_ascii(s): 
    return "".join(i for i in s if ord(i)<128)
    
def process_message(user, user_text_message, tokenizer, query=None):
    api = create_subprogram(tokenizer.api)
    if query:
        query.api = tokenizer.api
        query.request = user_text_message
        query.save() 
    try:
        result = getattr(api, tokenizer.program)(user, **tokenizer.arguments_dict)
    except: 
        result = getattr(api, "default")(user, **tokenizer.arguments_dict)
    return result
    
def create_subprogram(type):
    if type == "yelp": return Yelp() 
    if type == "maps": return Maps()
    if type == "wikipedia": return Wikipedia()
    if type == "attractions": return Attractions()
    if type == "onboard": return Onboard()
    if type == "limit": return Limit()
    if type == "news": return News()
    if type == "weather": return Weather()
    if type == "search": return Search()
    if type == "stock": return Stock()
    if type == "feedback": return Feedback()
    if type == "twitter": return Twitter()
    if type == "more": return More() 
    assert 0, "Invalid string " + type 
    return None 

if __name__ == '__main__':
    app.run(debug=True) 