from gmaps import Geocoding
from gmaps import Directions
import pprint
import re

direct = Directions()
geo = Geocoding()

TAG_RE = re.compile(r'<[^>]+>')
startLoc = '2121 S. El Camino Real, San Mateo CA'
endLoc = '820 E El Camino Real, Mountain View, CA'
DEFAULT = 'Hollingsworth Drive, Mountain View CA'
token = '\n'

def remove_tags(text):
    return TAG_RE.sub('', text)

def getDirections(start, end):
	direct = Directions()
	response = direct.directions(start, end)
	#pprint.pprint(response, indent=2)
	return response
    
# 1 for City, 0 for State 
def getLocation(start, typeLoc):
    response = getDirections(start, DEFAULT)
    address = response[0]['legs'][0]['start_address']
    tokens = address.split(', ')
    if typeLoc == 1:
    	return tokens[len(tokens) - 3]
    else:
    	return tokens[len(tokens) - 2][:2]

def getState(start):
	print getLocation(start, 0)

def getCity(start):
	print getLocation(start, 1)

def getDistance(start, end):
    response = getDirections(start, end)
    #pprint.pprint(response)
    return str(response[0]['legs'][0]['distance']['text'])

def getGeocode(location):
	response = geo.geocode(location)
	return str(response[0]['geometry']['location']['lat']) + ',' + str(response[0]['geometry']['location']['lng'])

def getLocation(lat, lng):
	location = geo.reverse(lat,lng);
	return location[0]['formatted_address'] 

def query(startLoc, endLoc):
	response = getDirections(startLoc, endLoc)
	instructionsList = response[0]['legs'][0]['steps']
	output = 'Directions to ' + endLoc + token
	counter = 0

	for insn in instructionsList:
		counter += 1
		cur_insn = remove_tags(insn['html_instructions'])
		cur_dist = insn['distance']['text']
		output += str(counter) + ' | ' + cur_insn + " | " + cur_dist + token
		#print cur_insn + " | " + cur_dist
	return output

