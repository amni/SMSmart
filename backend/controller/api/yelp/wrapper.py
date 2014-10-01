import sample

def query(location, radius = 5.0, category='restaurant'):
    print 'Arguments: ' + category + " | " + location
    return sample.query_api(category, location, radius, False, 1)

#output = query('Fairport, NY', 8.0, 'soccer')
#print output

def verbose(location, radius, index, category='restaurant'):
    return sample.query_api(category, location, radius, True, index)

def getLocation(location, radius, index, category='restaurant'):
	response = verbose(location, radius, index, category)
	parse = response.split(' | ')
	return parse[1]

#print query('San Jose, CA', 8.0, 'indian')
print verbose('San Jose, CA', 8.0, 1, 'indian')
#print getLocation('San Jose, CA', 8.0, 1, 'indian')