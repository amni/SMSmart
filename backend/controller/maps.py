from base import Base

class Maps(Base):
	def find_results(self, **kwargs):
		pass 
		
	def remove_tags(text):
	    return TAG_RE.sub('', text)

	def getDirections(start, end):
		direct = Directions()
		response = direct.directions(start, end)
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

	def getDistance(start, end):
	    response = getDirections(start, end)
	    pprint.pprint(response)
	    return str(response[0]['legs'][0]['distance']['text'])

	def query(startLoc, endLoc):
		print "Maps got query"
		response = getDirections(startLoc, endLoc)
		instructionsList = response[0]['legs'][0]['steps']

		output = 'Directions to ' + endLoc + token
		counter = 0


		for insn in instructionsList:
			counter += 1
			cur_insn = remove_tags(insn['html_instructions'])
			cur_dist = insn['distance']['text']
			output += str(counter) + '. ' + cur_insn + " | " + cur_dist + token
			#print cur_insn + " | " + cur_dist

		print
		print '---- Output -----'
		print output

		return output