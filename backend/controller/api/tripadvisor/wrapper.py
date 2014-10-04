import sys
sys.path.append('../maps/')
import maps
import requests 
import urllib2
import json
import pprint


API_KEY = 'b70c2406e27642e5b1fe2c21f3dfabc8'
API_ENDPOINT = 'http://api.tripadvisor.com/api/partner/2.0/map/*/attractions?key=' # * is long, lat coordinate

def getAttractions(location):
	geoLoc = maps.getGeocode(location)
	buildURL = API_ENDPOINT.split('*')
	url = buildURL[0] + geoLoc + buildURL[1] + API_KEY
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	#pprint.pprint(data, indent=2)

getAttractions('Nakholmen, Oslo, Norway')

