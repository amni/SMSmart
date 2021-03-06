from base import Base
import api.wrapper.weather_wrapper as weather_wrapper

class Weather(Base):
    def default(self, user, **kwargs):
        return self.search(user, **kwargs)

    def search(self, user, **kwargs):
        key = kwargs["key"]
        location = kwargs["near"]
        results = weather_wrapper.get_weather(location)
        if self.is_error(results):
            return self.get_error_response(results, key)
        
        joined_results = self.SEPARATOR_TOKEN.join(results)
        cleaned_results = self.prepend_key(key, joined_results)
        return self.split_result(cleaned_results) 