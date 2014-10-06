import sample
from restaurant import Restaurant
import maps

def query(location, distance = 5.0, category='restaurant'):
    return sample.query_api(category, location, distance, False, 1)

def query_geo(lat, lng, distance = 5.0, category='restaurant'):
    return query(str(maps.get_location_string(lat, lng)), distance, category)

def getLocation(location, distance, index, category='restaurant'):
    response = verbose(location, distance, index, category)
    parse = response.split(' | ')
    return parse[1]


