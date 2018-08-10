def higherLower(n):
	dp = [[0 for _ in range(n+1)]for _ in range(n+1)]
	# dp[i, j] = the answer for i, i+1, ..., j
	for gap in range(1,n):
		for i in range(1,n+1- gap):
			cost = float("inf")
			j = gap + i
			for k in range(i, j):
				cost = min(cost, k + max(dp[i][max(k-1,i)], dp[min(j,k+1)][j]))
			dp[i][j] =cost
	return dp[1][n]

print (higherLower(8))