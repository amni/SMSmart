import maps_wrapper as maps
import yelp
from restaurant import Restaurant

def query(location, distance = 5.0, category='restaurant', limit = 6):
    try:
        result = yelp.query_api(category, location, distance, False, 1, limit)
    except:
        result = '1'
    if result == None: #sometimes result will return None for an invalid category 
        result = '1'
    return result

def query_geo(lat, lng, distance = 5.0, category='restaurant', limit = 6):
    try:
        geo = str(lat)+','+str(lng)
        result = yelp.query_api_geo(category, geo, distance, False, 1, limit)
    except:      
        result = '1'
    if result == None:
        result = '1'        
    return result

