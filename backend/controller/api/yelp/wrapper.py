import maps 
import sample
from restaurant import Restaurant

def query(location, distance = 5.0, category='restaurant', search_limit = 3):
    return sample.query_api(category, location, distance, False, 1, search_limit)

def query_geo(lat, lng, distance = 5.0, category='restaurant', search_limit = 5):
    #print str(maps.get_location_string(lat, lng)
    geo = str(lat)+','+str(lng)
    return sample.query_api_geo(category, geo, distance, False, 1, search_limit)

def getLocation(location, distance, index, category='restaurant'):
    response = verbose(location, distance, index, category)
    parse = response.split(' | ')
    return parse[1]


#print(query_geo(37.253,-121.90))