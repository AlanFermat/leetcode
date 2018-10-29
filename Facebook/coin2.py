from collections import defaultdict as dd
def change(amount, coins):
	"""
	:type amount: int
	:type coins: List[int]
	:rtype: int
	"""
	dp = dd(int)
	dp[0] = 1
	coins = sorted(coins)
	for coin in coins:
		for j in range(1, amount + 1):
			if j >= coin:
				dp[j] += dp[j-coin]
	return dp[amount]





	
	

amount = 500
coins = [1,2,5]
print (change(amount, coins))