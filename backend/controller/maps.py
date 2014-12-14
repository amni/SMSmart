from base import Base
import api.travel.maps_wrapper as maps_wrapper
from models import User, Query

class Maps(Base):
    def default(self, user, **kwargs):
        return self.directions(user, **kwargs)

    def directions(self, user, **kwargs):
        try: 
            if not "from" or not "to" in kwargs:
                return "Please make the text in the form of maps directions: from:(your starting location) to: (your destination)"
            if "mode" in kwargs:
                response = maps_wrapper.get_directions(kwargs["from"], kwargs["to"], kwargs["mode"])
            else:
                response = maps_wrapper.get_directions(kwargs["from"], kwargs["to"])
            instructionsList = response[0]['legs'][0]['steps']
            key = kwargs["key"]
            #output = 'Directions to ' + kwargs["to"] + "\n"
            output = ''
            counter = 0

            for insn in instructionsList:
                counter += 1
                cur_insn = maps_wrapper.remove_tags(insn['html_instructions'])
                cur_dist = insn['distance']['text']
                output += str(counter) + '|' + cur_insn + '|' + cur_dist + '^'
            result = key + "^" + output
            return result[:-1]
        except:
            return "Couldn't find a route please try with more specific locations"

    def help(self, user, **kwargs):
        return """
        Here is an example text!\n
        To get directions from Mountain View to San Francisco, text - maps: from: Mountain View, CA to: San Francisco, CA
        Don't forget to use colons!
        """