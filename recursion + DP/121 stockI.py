def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	if not prices:
		return 0
	max_pro = 0
	min_price = float("inf")
	for price in prices:
		if price < min_price:
			min_price = price
		else:
			max_pro = max(max_pro, price - min_price)
	return max_pro