import pyowm

owm = pyowm.OWM('d78288c387e97c415463a6e1dcc32e32')
  
def get_weather(location):
    try:
        observation = owm.weather_at_place(location).get_weather()
        temperatures =  observation.get_temperature("fahrenheit")
        status = observation.get_status()
        cur_temp = temperatures["temp"]
        result = get_result([location, status, str(cur_temp)])
    except: 
        result = 1
    return result


def get_result(variables):
    return "|".join(variables)
