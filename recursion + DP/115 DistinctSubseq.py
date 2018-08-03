def numDistinct(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: int
	"""
	n = len(s)
	m = len(t)
	if not t and not s:
		return 1
	if not t or not s:
		return 0
	if m == 1:
		return s.count(t)
	dp = [[0 for _ in range(n)] for _ in range(m)]
	dp[m-1][n-1] = (s[n-1] == t[m-1]) + 0
	print (dp)
	for j in range(n-2, m-2, -1):
		dp[m-1][j] = dp[m-1][j+1] + (t[m-1] == s[j])
	print (dp)
	for idx in range(m-2, -1, -1):
		for j in range(n-m+idx, -1, -1):
			if t[idx] == s[j]:
				dp[idx][j] += dp[idx+1][j+1] + dp[idx][j+1]
			else:
				dp[idx][j] = dp[idx][j+1]
	print (dp)
	return dp[0][0]

s = "babgbag"
t = "bag"
print (numDistinct(s,t))