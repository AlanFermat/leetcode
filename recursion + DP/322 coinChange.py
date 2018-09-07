def coinChange(coins, amount):
	"""
	:type coins: List[int]
	:type amount: int
	:rtype: int
	"""
	if not amount:
		return 0 
	if not coins or amount < min(coins):
		return -1
	dp = [float("inf") for _ in range(amount+1)]
	dp[0] = 0
	for c in range(amount+1):
		min_val = float('inf')
		for t in coins:
			if c-t >= 0 and dp[c-t] < min_val:
				min_val = dp[c-t]
		if min_val < float('inf'):
			dp[c] = min_val + 1
	if dp[amount] == float("inf"):
		return -1
	return dp[amount]