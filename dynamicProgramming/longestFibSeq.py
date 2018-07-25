def longestFib(s):
	n = len(s)
	mapping = {}
	for idx, item in enumerate(s):
		mapping[item] = idx
	print mapping
	dp = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(1, n-1):
		for j in range(i+1, n):
			k = mapping.get(s[j] -s[i], -1)
			if k >= 0 and k < i:
				if dp[k][i] == 0:
					dp[i][j] = 3
				else:
					dp[i][j] = dp[k][i] + 1
	maxVal = 0
	for i in range(n):
		for j in range(n):
			if dp[i][j] > maxVal:
				maxVal = dp[i][j]
	return maxVal


s = [1,3,7,11,12,14,18]
print longestFib(s)