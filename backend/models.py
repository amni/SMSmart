from mongoengine import *
import datetime


class Query(Document):
	query_id = StringField()
	api = StringField()
	request = StringField()
	response = StringField()
	date_created = DateTimeField(default=datetime.datetime.now) 

class User(Document):
	phone_number = StringField(required=True, unique=True)
	queries = ListField(ReferenceField(Query))
	date_created = DateTimeField(default=datetime.datetime.now)
