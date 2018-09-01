def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	if not prices or len(prices) == 1:
		return 0
	dp1, dp2, dp3 = 0,0, -prices[0]
	for p in prices:
		dp2, dp3, dp1 = max(dp1,dp2), max(dp2-p, dp3), dp3+p
	return max(dp1, dp2)