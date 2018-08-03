def longestPalindromeSubseq(s):
	"""
	:type s: str
	:rtype: int
	"""

	## O(n^2) space 
	# n = len(s)
	# dp = [[0 for _ in range(n)] for _ in range(n)]
	# for i in range(n):
	# 	dp[i][i] = 1
	# for i in range(n-1):
	# 	if s[i] == s[i+1]:
	# 		dp[i][i+1] = 2
	# 	else:
	# 		dp[i][i+1] = 1
	# for i in range(n-3, -1, -1):
	# 	for j in range(i+2, n):
	# 		if s[i] == s[j]:
	# 			dp[i][j] = 2 + dp[i+1][j-1]
	# 		else:
	# 			dp[i][j] = max(dp[i+1][j], dp[i][j-1])
	# return dp[0][n-1]

	## O(n) space
	if not s:
		return 0
	n = len(s)
	if n == 1:
		return 1
	dp = [[0 for _ in range(n)] for _ in range(2)]
	for i in range(n):
		dp[0][i] = 1
	for i in range(n-1):
		if s[i] == s[i+1]:
			dp[1][i+1] = 2
		else:
			dp[1][i+1] = 1
	flag = 0
	for diff in range(2, n):
		flag = 1 - flag
		for idx in range(n-1, diff-1, -1):
			if s[idx] == s[idx - diff]:
				dp[1-flag][idx] = 2 + dp[1-flag][idx-1]
			else:
				dp[1-flag][idx] = max(dp[flag][idx], dp[flag][idx-1])
	return dp[1-flag][n-1]

s = "ccdccf"

print (longestPalindromeSubseq(s))








	
	
		
		