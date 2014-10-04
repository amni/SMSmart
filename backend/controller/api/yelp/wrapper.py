import sample
from restaurant import Restaurant

def query(location, distance = 5.0, category='restaurant'):
    # print 'Arguments: ' + category + " | " + location
    return sample.query_api(category, location, distance, False, 1)

#output = query('Fairport, NY', 8.0, 'soccer')
#print output

def verbose(location, distance, index, category='restaurant'):
    return sample.query_api(category, location, distance, True, index)

def getLocation(location, distance, index, category='restaurant'):
    response = verbose(location, distance, index, category)
    parse = response.split(' | ')
    return parse[1]

ret = query('San Jose, CA', 8.0, 'indian')


#print verbose('San Jose, CA', 8.0, 1, 'indian')
#print query('San Jose, CA', 8.0, 'indian')
# print verbose('San Jose, CA', 8.0, 1, 'indian')
#print getLocation('San Jose, CA', 8.0, 1, 'indian')