from base import Base
import api.wrapper.maps_wrapper as maps_wrapper
from models import User, Query

class Maps(Base):
    def default(self, user, **kwargs):
        return self.directions(user, **kwargs)

    def directions(self, user, **kwargs):
        key = kwargs["key"]
        if not "from" or not "to" in kwargs:
            return "Please make the text in the form of maps directions: from:(your starting location) to: (your destination)"
        if "mode" in kwargs:
            response = maps_wrapper.get_directions(kwargs["from"], kwargs["to"], kwargs["mode"])
        else:
            response = maps_wrapper.get_directions(kwargs["from"], kwargs["to"])
        
        print response
        if self.is_error(response):
            result = key+"^"+response
            return self.split_result(result)

        instructionsList = response[0]['legs'][0]['steps']
        output = ''
        counter = 0
        for insn in instructionsList:
            counter += 1
            cur_insn = maps_wrapper.remove_tags(insn['html_instructions'])
            cur_dist = insn['distance']['text']
            output += str(counter) + '|' + cur_insn + '|' + cur_dist + '^'
        result = (key + self.OK + "^" + output)[:-1]    # do this to remove the last excess ^
        return self.split_result(result)
