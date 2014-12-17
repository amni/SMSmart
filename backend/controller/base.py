from models import User

class Base(object):
	def find_results(self, **kwargs):
		pass

	def distribute(self, results):
		pass

	def save(self, user, results):
		new_query = Query(response = results)
		return new_query
