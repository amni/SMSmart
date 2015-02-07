from mongoengine import *
import datetime


class Query(Document):
	query_id = StringField()
	api = StringField()
	request = StringField()
	response = StringField()
	date_created = DateTimeField(default=datetime.datetime.now) 

	def is_less_than_month_old(self):
		"""Checks that month and year of query is same as today's date"""
		today = datetime.date.today()
		return (today.month == self.date_created.month) and (today.year == self.date_created.year)


class Comment(Document):
	content = StringField()

class User(Document):
	phone_number = StringField(required=True, unique=True)
	queries = ListField(ReferenceField(Query))
	date_created = DateTimeField(default=datetime.datetime.now)
	text_limit = IntField(default=150)
	email = StringField()
	comments = ListField(ReferenceField(Comment))
	
	def is_over_limit(self):
		return self.text_limit <= len(self.queries) 

