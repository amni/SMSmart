from base import Base
import api.wrapper.stock_wrapper as stock_wrapper

class Stock(Base):
    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        key = kwargs["key"]
        symbol = kwargs["symbol"]
        results = stock_wrapper.get_share_price(symbol)
        if self.is_error(results):
            return self.get_error_response(results, key)
        joined_results = self.SEPARATOR_TOKEN.join(results)        
        cleaned_results = self.prepend_key(key, joined_results)
        return self.split_result(cleaned_results) 