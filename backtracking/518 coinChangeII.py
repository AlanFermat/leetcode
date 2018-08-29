def change(amount, coins):
	"""
	:type amount: int
	:type coins: List[int]
	:rtype: int
	"""
	def helper(amount, coins, path, result):
		if sum(path) == amount:
			result.append(path)
			return 
		if sum(path) + coins[start] > amount:
			return 
		for 

	res = []
	helper(amount, coins,[],res)
	return res

amount = 5
coins = [1,2,5]
print change(amount, coins)

