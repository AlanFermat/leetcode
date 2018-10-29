def minCostII(costs):
	"""
	:type costs: List[List[int]]
	:rtype: int
	"""
	if not costs or not costs[0]:
		return 0
	n = len(costs)
	k = len(costs[0])
	dp = [[0 for _ in range(k)] for _ in range(n)]
	for col in range(k):
		dp[0][col] = costs[0][col]
	def getMin(mat):
		min_val = float('inf')
		min_col = 0
		for pos in range(len(mat)):
			if min_val > mat[pos]:
				min_val = mat[pos]
				min_col = pos
		return min_val, min_col 
	
	def getMinExclude(mat, col):
		min_val = float('inf')
		for pos in range(len(mat)):
			if pos != col:
				min_val = min(mat[pos], min_val)
		return min_val
	
	for idx in range(1,n):
		min_val, min_col = getMin(dp[idx-1])
		getVal = getMinExclude(dp[idx-1], min_col)
		for col in range(k):
			if col != min_col:
				dp[idx][col] = costs[idx][col] + min_val
			else:
				dp[idx][col] =  getVal + costs[idx][col]
	return min(dp[n-1])


costs = [[15,17,15,20,7,16,6,10,4,20,7,3,4],[11,3,9,13,7,12,6,7,5,1,7,18,9]]

print (minCostII(costs))