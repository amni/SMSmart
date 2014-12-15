import maps_wrapper as maps
import yelp
from restaurant import Restaurant

def query(location, distance = 5.0, category='restaurant', limit = 6):
    return yelp.query_api(category, location, distance, False, 1, limit)

def query_geo(lat, lng, distance = 5.0, category='restaurant', limit = 6):
    #print str(maps.get_location_string(lat, lng)
    geo = str(lat)+','+str(lng)
    return yelp.query_api_geo(category, geo, distance, False, 1, limit)

def getLocation(location, distance, index, category='restaurant'):
    response = verbose(location, distance, index, category)
    parse = response.split(' | ')
    return parse[1]
