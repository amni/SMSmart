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


class User(Document):
	phone_number = StringField(required=True, unique=True)
	queries = ListField(ReferenceField(Query))
	date_created = DateTimeField(default=datetime.datetime.now)
	query_limit = IntField(default=30)

	def get_num_queries_this_month(self):
		return len([query for query in self.queries if query.is_less_than_month_old()])

	def is_over_limit(self):
		return self.get_num_queries_this_month() > self.query_limit
