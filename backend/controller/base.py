from models import User

class Base(object):
	def find_results(self, **kwargs):
		pass

	def split_result(self, results):
		return results

	def save(self, user, results):
		new_query = Query(response = results)
		return new_query
