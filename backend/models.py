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

class Referral(Document):
	phone_number = StringField(required=True)
	date_referred = DateTimeField() 
	is_legal_referral = BooleanField(default=False)

	def check_legal_referral(self):
		if not self.is_legal_referral:
			user_signup = User.objects(phone_number=str(self.phone_number)).first()
			if user_signup:
				self.is_legal_referral = user_signup.date_created > self.date_referred
				self.save()
		return self.is_legal_referral

class Comment(Document):
	content = StringField()

class PageItem(Document):
	content = StringField()


class TextPart(Document):
	content = StringField()
	num = IntField()

class Text(Document):
	key = StringField()
	total_expected = IntField()
	text_parts = ListField(ReferenceField(TextPart))

class Page(Document):
	items = ListField(ReferenceField(PageItem))
	retrieval_key = StringField(required = True) 
	current_index = IntField(default = 0)

class Auth(Document):
	api = StringField() 
	secret = StringField()
	access = StringField()

class User(Document):
	phone_number = StringField(required=True, unique=True)
	queries = ListField(ReferenceField(Query))
	date_created = DateTimeField(default=datetime.datetime.now)
	text_limit = IntField(default=150)
	email = StringField()
	comments = ListField(ReferenceField(Comment))
	referrals = ListField(ReferenceField(Referral))
	auths = ListField(ReferenceField(Auth))
	pages = ListField(ReferenceField(Page))
	
	def is_over_limit(self):
		return self.text_limit <= len(self.queries) 

	def get_auth(self, api):
		for auth in reversed(self.auths):
			if auth.api == api:
				return auth 
		return None 

	def get_page(self, retrieval_key):
		for page in self.pages:
			if page.retrieval_key == retrieval_key:
				return page
		return None 
