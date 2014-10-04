class Restaurant:

	def __init__(self, name, location, distance, phone, rating, isClosed):
		self.name = name
		self.location = location
		self.distance = distance
		self.phone = phone
		self.rating = rating
		self.isClosed = isClosed 

	def to_string(self):
		return self.name + ' | ' +  self.location +  ' | ' + self.distance + ' | ' + self.phone + ' | ' + self.rating + ' | ' + self.isClosed




