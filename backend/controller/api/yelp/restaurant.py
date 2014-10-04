class Restaurant:

    def __init__(self, name, location, phone, rating, isClosed):
        self.name = name
        self.location = location
        self.phone = phone
        self.rating = rating
        self.isClosed = isClosed 

    def to_string(self):
        return self.name + ' | ' +  self.location + ' | ' + self.phone + ' | ' + self.rating + ' | ' + self.isClosed

