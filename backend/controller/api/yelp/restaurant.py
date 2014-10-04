class Restaurant:

    def __init__(self, counter, name, location, phone, rating, isClosed):
        self.counter = counter
        self.name = name
        self.location = location
        self.phone = phone
        self.rating = rating
        self.isClosed = isClosed 

    def to_string(self):
        return str(self.counter) + ' | ' + self.name + ' | ' + self.rating + ' | ' + self.isClosed

    def to_string_verbose(self):
        return str(self.counter) + ' | ' + self.name + ' | ' +  self.location + ' | ' + self.phone + ' | ' + self.rating + ' | ' + self.isClosed        
