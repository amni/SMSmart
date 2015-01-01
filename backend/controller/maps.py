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
        if self.is_error(response):
            result = response+key+self.CARROT_TOKEN+self.EMPTY_MSG
            return self.split_result(result)

        instructionsList = response[0]['legs'][0]['steps']
        output = self.EMPTY_MSG
        geo_output = self.EMPTY_MSG
        counter = 0
        for insn in instructionsList:
            counter += 1
            html_insn = insn['html_instructions'].replace('Destination', ' - Destination') # hack // yelp api missing a space
            cur_insn = maps_wrapper.remove_tags(html_insn)
            cur_dist = insn['distance']['text']
            cur_lat = str(insn['end_location']['lat'])
            cur_lng = str(insn['end_location']['lng'])
            geo_output += str(counter) + self.SEPARATOR_TOKEN + cur_lat + ',' + cur_lng + self.CARROT_TOKEN
            output += str(counter) + self.SEPARATOR_TOKEN + cur_insn + self.SEPARATOR_TOKEN + cur_dist + self.CARROT_TOKEN
        result = (self.OK + key + self.CARROT_TOKEN + output)[:-1]    # do this to remove the last excess ^

        if "geo" in kwargs:
            if kwargs["geo"].upper() == self.TRUE_TOKEN:
                result += (self.GEO_TOKEN + geo_output)[:-1]

        return self.split_result(result)
