from yahoo_finance import Share

def get_share_price(stock_symbol):
	try:
		stock_symbol = stock_symbol.lower()
		stock = Share(stock_symbol)
		opening_price = stock.get_open()
		cur_price = stock.get_price()
		pe_ratio = stock.get_price_earnings_ratio()
		market_cap = stock.get_market_cap()
		result = [stock_symbol, str(cur_price), str(opening_price), str(pe_ratio), str(market_cap)]
	except:
		result = "1"
	return result
