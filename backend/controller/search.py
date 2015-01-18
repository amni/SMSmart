from base import Base
import api.wrapper.search_wrapper as search_wrapper

class Search(Base):
    def default(self, user, **kwargs):
        return self.query(user, **kwargs)

    def query(self, user, **kwargs):
        key = kwargs["key"]
        term = kwargs["term"]
        results = search_wrapper.perform_search(term)
        if self.is_error(results):
            return self.get_error_response(results, key)
        cleaned_results = self.get_result_list(key, results)
        return self.split_result(cleaned_results)

