from yahoo_finance import Share

def get_share_price(stock_symbol):
	try:
		stock_symbol = stock_symbol.lower()
		stock = Share(stock_symbol)
		opening_price = stock.get_open()
		cur_price = stock.get_price()
		result = get_result([stock_symbol, str(cur_price), str(opening_price)])
	except:
		result = "1"
	return result

def get_result(variables):
    return "|".join(variables)