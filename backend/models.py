from mongoengine import *


class User(Document):
	phone_number = StringField(required=True, unique=True)

class Variable(Document):
	keyword = StringField(required=True)
	value = StringField()
	type = StringField() 
	program = StringField() 
	user = ReferenceField(User)