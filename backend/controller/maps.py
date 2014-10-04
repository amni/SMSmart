from base import Base
from gmaps import Directions
from gmaps import Geocoding
import re


class Maps(Base):
    def find_results(self, **kwargs):
        pass 
        
    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', text)

    def get_directions(self, start, end):
        direct = Directions()
        response = direct.directions(start, end)
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
        if not "from" or not "to" in kwargs:
            return "Please make the text in the form of maps directions: from:location to:location"
        response = self.get_directions(kwargs["from"], kwargs["to"])
        instructionsList = response[0]['legs'][0]['steps']

        output = 'Directions to ' + kwargs["to"] + "\n"
        counter = 0

        for insn in instructionsList:
            counter += 1
            cur_insn = self.remove_tags(insn['html_instructions'])
            cur_dist = insn['distance']['text']
            output += str(counter) + '. ' + cur_insn + " | " + cur_dist + "\n"

        return output