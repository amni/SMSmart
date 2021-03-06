import maps_wrapper as maps    # works for this class 
import requests 
import urllib2
import json
from attraction import Attraction

API_KEY = 'b70c2406e27642e5b1fe2c21f3dfabc8'
API_ENDPOINT = 'http://api.tripadvisor.com/api/partner/2.0/map/*/attractions?key=' # * is long, lat coordinate

def query(location):
    data = make_request(location)
    ret = []
    counter = 1
    for attraction in data:
        ret.append(build_object(attraction, counter))
        counter += 1
    return ret

def query_geo(lat, lng):
    return query(str(maps.get_location_string(lat, lng)))

def make_request(location):
    geoLoc = maps.getGeocode(location)
    buildURL = API_ENDPOINT.split('*')
    url = buildURL[0] + geoLoc + buildURL[1] + API_KEY
    resp = requests.get(url=url)
    return json.loads(resp.text)['data']

def build_object(attraction, counter):
    address_obj = attraction['address_obj']
    name = attraction['name']
    recommend = attraction['percent_recommended']
    rating = attraction['rating']
    distance = attraction['distance']
    address = address_obj['address_string'] + ', ' + address_obj['city'] + ', ' + address_obj['country']
    attraction_type = attraction['attraction_types'][0]['localized_name'] if attraction['attraction_types'] else ''
    return Attraction(str(counter), name, recommend, rating, distance, address, attraction_type)
