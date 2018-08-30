def maxProfit(prices, fee):
	"""
	:type prices: List[int]
	:type fee: int
	:rtype: int
	"""
	if not prices:
		return 0
	n = len(prices)
	s0 = [0 for _ in range(n)]
	s1 = [0 for i in range(n)]
	for l in range(n):
		s1[l] = -prices[l]
	for i in range(1,n):
		s0[i] = max(s0[i-1], s1[i-1] + prices[i] - fee)
		s1[i] = max(s1[i-1], s0[i-1] - prices[i])
	return max(s0[-1],s1[-1])