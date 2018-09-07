def longestIncreasingPath(matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: int
	"""
	if not matrix or not matrix[0]:
		return 0
	m, n = len(matrix), len(matrix[0])
	dp = [[0 for _ in range(n)] for _ in range(m)]
	
	def dfs(i,j, m,n, dp, matrix):
		if dp[i][j]:
			return dp[i][j]
		else:
			count = 0
			if i+1 < m and matrix[i][j] < matrix[i+1][j]:
				count = max(dfs(i+1,j, m,n, dp, matrix), count)
			if i-1 >-1 and matrix[i][j] < matrix[i-1][j]:
				count = max(dfs(i-1,j, m,n, dp, matrix), count)
			if j+1 < n and matrix[i][j] < matrix[i][j+1]:
				count = max(dfs(i,j+1, m,n, dp, matrix), count)
			if j-1 >-1 and matrix[i][j] < matrix[i][j-1]:
				count = max(dfs(i,j-1, m,n, dp, matrix), count)
			dp[i][j] = count + 1
			return dp[i][j]
			
	max_l = 0 
	for i in range(m):
		for j in range(n):
			max_l = max(dfs(i,j, m, n, dp, matrix), max_l)
	return max_l