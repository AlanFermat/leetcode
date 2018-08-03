def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	if not prices:
		return 0
	# max profit 
	maxPro = 0
	# buy and sell dates
	buy = [float('inf'), -1]
	idx = 0
	n = len(prices)
	while idx < n:
		if prices[idx] < buy[0]:
			buy[0] = prices[idx]
			buy[1] = idx
		maxPro = max(maxPro, prices[idx] - buy[0])
		idx +=1 
	return maxPro

prices = [7,0,4,2,5]
print (maxProfit(prices))
