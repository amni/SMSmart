from gmaps import Geocoding
from gmaps import Directions
import gmaps
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

# supported modes include driving, walking, bicycling, transit 
def get_directions(start, end, transport="driving"):
    try:
        direct = Directions()
        response = direct.directions(start, end, mode=transport)
    except gmaps.errors.GmapException as ex:
        response = '1'
    except:
        response = '2'
    return response
    
# 1 for City, 0 for State 
def get_location(start, typeLoc):
    response = get_directions(start, DEFAULT)
    address = response[0]['legs'][0]['start_address']
    tokens = address.split(', ')
    if typeLoc == 1:
        return tokens[len(tokens) - 3]
    else:
        return tokens[len(tokens) - 2][:2]

def get_state(start):
    return get_location(start, 0)

def get_city(start):
    return get_location(start, 1)

def get_distance(start, end):
    response = get_directions(start, end)
    return str(response[0]['legs'][0]['distance']['text'])

def get_geocode(location):
    response = geo.geocode(location)
    return str(response[0]['geometry']['location']['lat']) + ',' + str(response[0]['geometry']['location']['lng'])

def get_location_string(lat, lng):
    location = geo.reverse(lat,lng);
    return location[0]['formatted_address'] 

