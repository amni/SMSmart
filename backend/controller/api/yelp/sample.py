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
import sys
sys.path.append('../maps/')
import oauth2
import maps
from restaurant import Restaurant


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 10
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'
token = '\n'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = 'vCXEpMiao6c-HTNuWtG_mA'
CONSUMER_SECRET = '9jRGBwC46kIgGSNtcqoQAXpB4Dc'
TOKEN = 'eslr8aJfdlBV7u9CogEy1QnnjgphiGsc'
TOKEN_SECRET = 'n2oQBgUhBUq-PNjKxXvmlysmRwo'


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    encoded_params = urllib.urlencode(url_params)

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

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def search(term, location, limit, radius):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'term': term,
        'location': location,
        'limit': SEARCH_LIMIT,
        'radius': radius
    }

    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def get_business(business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)

def query_api(term, location, radius, verbose, index):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, location, 1, radius)
    businesses = response.get('businesses')

    if not businesses:
        return
    return getLocations(businesses, location, verbose, index);
    #response = get_business(business_id)
    #print 'Result for business "{0}" found:'.format(business_id)
    #print response['location']['address'][0] + ', ' + response['location']['city'] + ' ' + response['location']['postal_code']

def formatPhone(phone):
    areaCode = '(' + phone[:3] + ') '
    begin = phone[3:6]
    end = phone[-4:]
    return areaCode + begin + '-' + end

# z
#Todo: make robust to missing fields
def buildResponse(response, counter, location, verbose):
    count = str(counter) + '. '

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
    #neighborhood = response['location']['neighborhoods'][0]

    ret = Restaurant(counter, name, endLocation, phone, rating, isClosed)
    return ret
    """
    if (not verbose):
        return count + name + ' | '  + phone + ' | ' + rating  + token
    else:
        return name + ' | ' +  endLocation +  ' | ' + distance + ' | ' + phone + ' | ' + rating + ' | ' + isClosed + token"""

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


