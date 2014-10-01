import sample

def query(location, radius, category='restaurant'):
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

print(getLocation('San Jose, CA', 8.0, 3, 'food'))