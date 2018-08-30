def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	if not prices:
		return 0
	max_pro = 0
	for i in range(len(prices)-1):
		diff = prices[i+1] - prices[i]
		max_pro += max(0, diff)
	return max_pro