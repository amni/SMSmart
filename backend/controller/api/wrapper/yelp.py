# -*- coding: utf-8 -*-
"""
Yelp API v2.0 code sample.

This program demonstrates the capability of the Yelp API version 2.0
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.

Please refer to http://www.yelp.com/developers/documentation for the API documentation.

This program requires the Python oauth2 library, which you can install via:
`pip install -r requirements.txt`.

Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
import argparse
import json
import pprint
import sys
import urllib
import urllib2
import oauth2
import maps_wrapper as maps
from restaurant import Restaurant
from urllib2 import HTTPError
import unicodedata

API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'
token = '\n'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = 'vCXEpMiao6c-HTNuWtG_mA'
CONSUMER_SECRET = '9jRGBwC46kIgGSNtcqoQAXpB4Dc'
TOKEN = 'eslr8aJfdlBV7u9CogEy1QnnjgphiGsc'
TOKEN_SECRET = 'n2oQBgUhBUq-PNjKxXvmlysmRwo'


def request(host, path, url_params=None):
    url_params = url_params or {}
    encoded_params = urllib.urlencode(url_params)
    path = unicodedata.normalize('NFKD', unicode(path)).encode('ascii','ignore')
    url = 'http://{0}{1}?{2}'.format(host, path, encoded_params)

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    try:
        conn = urllib2.urlopen(signed_url, None)
        response = json.loads(conn.read())
        conn.close()
    except HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))

    return response

def search(term, location, limit, radius):
    url_params = {
        'term': term,
        'location': location,
        'limit': limit,
        'radius': radius
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def search_geo(term, geo, limit, radius):
    url_params = {
        'term': term,
        'll': geo,
        'limit': limit,
        'radius': radius
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def get_business(business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path)

def query_api_geo(term, geo, radius, verbose, index, search_limit):
    response = search_geo(term, geo, search_limit, radius)
    businesses = response.get('businesses')
    if not businesses:
        return
    return getLocations(businesses, geo, verbose, index);

def query_api(term, location, radius, verbose, index, search_limit):
    response = search(term, location, search_limit, radius)
    businesses = response.get('businesses')
    if not businesses:
        return
    return getLocations(businesses, location, verbose, index);

def formatPhone(phone):
    areaCode = '(' + phone[:3] + ') '
    begin = phone[3:6]
    end = phone[-4:]
    return areaCode + begin + '-' + end

def buildResponse(response, counter, location, verbose):
    name = response['name']
    if 'categories' in response:
        name +=  ' (' + response['categories'][0][0]+ ')' 
    if 'location' in response:
        endLocation = response['location']['display_address'][0] + ', ' + response['location']['city'] + ', ' + response['location']['state_code'] + ' ' + response['location']['postal_code']
    else:
        endLocation = 'location unavailable'
    if 'phone' in response:
        phone = formatPhone(str(response['phone'])) 
    else:
        phone = 'phone unavailabe'
    if 'rating' in response:
        rating = str(response['rating']) + " stars" 
    else:
        rating = 'rating unavailable'
    status = 'open' if (str(response['is_closed']) == 'False') else 'closed'
    isClosed = status 
    ret = Restaurant(counter, name, endLocation, phone, rating, isClosed)
    return ret

def getLocations(businesses, location, verbose, index):
    output = []
    counter = 0
    if verbose:
        business = businesses[int(index) - 1]
        bizId = business['id']
        response = get_business(bizId)
        #pprint.pprint(response, indent=2)
        output.append(buildResponse(response, counter, location, verbose))
    else:
        for business in businesses:
            counter += 1
            bizId = business['id']
            response = get_business(bizId)
            #pprint.pprint(response, indent=2)
            output.append(buildResponse(response, counter, location, verbose))
    return output 


