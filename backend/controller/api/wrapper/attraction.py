class Attraction:

    def __init__(self, counter, name, percent_recommended, rating, distance, address, attraction_type):
        self.counter = counter
        self.name = name
        self.percent_recommended = percent_recommended
        self.rating = rating
        self.distance = distance
        self.address = address
        self.attraction_type = attraction_type

    def to_string(self):
        return str(self.counter) + ' | ' + self.name + ' | ' + self.distance + ' | ' + self.attraction_type

    def to_string_verbose(self):
        return str(self.counter) + ' | ' + self.name + ' | ' +  str(self.percent_recommended) + ' | ' + str(self.rating) + ' | ' + self.distance + ' | ' + self.address + ' | ' + self.attraction_type        
