from mongoengine import *


class Query(Document):
	query_id = StringField()
	api = StringField()
	request = StringField()
	response = StringField() 

class User(Document):
	phone_number = StringField(required=True, unique=True)
	queries = ListField(ReferenceField(Query))
