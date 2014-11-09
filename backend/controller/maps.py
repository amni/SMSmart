from base import Base
from gmaps import Directions
from gmaps import Geocoding
import re

class Maps(Base):
    def default(self, user, **kwargs):
        return self.directions(user, **kwargs)

    def find_results(self, **kwargs):
        pass 
    
    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', text)

    # supported modes include driving, walking, bicycling, transit 
    def get_directions(self, start, end, transport="driving"):
        direct = Directions()
        response = direct.directions(start, end, mode=transport)
        return response
        
    # 1 for City, 0 for State 
    def get_location(self, start, typeLoc):
        response = self.get_directions(start, DEFAULT)
        address = response[0]['legs'][0]['start_address']
        tokens = address.split(', ')
        if typeLoc == 1:
            return tokens[len(tokens) - 3]
        else:
            return tokens[len(tokens) - 2][:2]

    def get_distance(self, start, end):
        response = get_directions(start, end)
        pprint.pprint(response)
        return str(response[0]['legs'][0]['distance']['text'])

    def directions(self, user, **kwargs):
        try: 
            if not "from" or not "to" in kwargs:
                return "Please make the text in the form of maps directions: from:(your starting location) to: (your destination)"
            if "mode" in kwargs:
                response = self.get_directions(kwargs["from"], kwargs["to"], kwargs["mode"])
            else:
                response = self.get_directions(kwargs["from"], kwargs["to"])
            instructionsList = response[0]['legs'][0]['steps']
            key = kwargs["key"]
            #output = 'Directions to ' + kwargs["to"] + "\n"
            output = ''
            counter = 0

            for insn in instructionsList:
                counter += 1
                cur_insn = self.remove_tags(insn['html_instructions'])
                cur_dist = insn['distance']['text']
                output += str(counter) + '|' + cur_insn + '|' + cur_dist + '^'
            return key + "^" + output
        except:
            return "Couldn't find a route please try with more specific locations"

    def help(self, user, **kwargs):
        return """
        Here is an example text!\n
        To get directions from Mountain View to San Francisco, text - maps: from: Mountain View, CA to: San Francisco, CA
        Don't forget to use colons!
        """