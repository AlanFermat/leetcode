def calculateMinimumHP(dungeon):
	"""
	:type dungeon: List[List[int]]
	:rtype: int
	"""
	num = dungeon
	m = len(num)
	n = len(num[0])
	dp = [[-float('inf') for _ in range(n)] for _ in range(m)]
	dp[m-1][n-1] = max(-num[m-1][n-1]+1,1)
	for col in range(n-2, -1, -1):
		if num[m-1][col] <= 0:
			dp[m-1][col] = dp[m-1][col+1] - num[m-1][col]
		if num[m-1][col] > 0:
			dp[m-1][col] = max(dp[m-1][col+1] - num[m-1][col], 1)
	for row in range(m-2, -1, -1):
		if num[row][n-1] <= 0:
			dp[row][n-1] = dp[row+1][n-1] - num[row][n-1]
		else:
			dp[row][n-1] = max(dp[row+1][n-1]-num[row][n-1],1)
	for r in range(m-2, -1, -1):
		for c in range(n-2, -1, -1):
			if num[r][c] <=0:
				dp[r][c] = min(dp[r+1][c], dp[r][c+1]) - num[r][c]
			else:
				dp[r][c] = max(min(dp[r+1][c], dp[r][c+1]) - num[r][c],1)
	print (dp)
	return dp[0][0]


d = [[2],[1]]
calculateMinimumHP(d)

