def decode(s):
	if not s or s.find("00") >=0 or s == "0":
		return 0
	l = list(s)
	m = len(s)
	idx = 0
	while idx < m-1:
		if idx == 0 and not int(l[idx]):
			return 0
		elif not int(l[idx+1]):
			if l[idx] not in ["1","2"]:
				return 0
			del l[idx+1]
			del l[idx]
			m -= 2
		else:
			idx += 1
	if l:
		st = "".join(l)
		n =  len(st)
		dp = [[0 for _ in range(n)] for _ in range(n)]
		for i in range(n):
			dp[i][i] = 1
		for i in range(n-1):
			dp[i][i+1] = dp[i][i] + (0< int(st[i:i+2]) < 27)
		for i in range(n-1, -1, -1):
			for j in range(i+2, n):
				dp[i][j] += dp[i][j-1]
				if 0< int(st[j-1:j+1]) < 27:
					dp[i][j] += dp[i][j-2]
		return dp[0][n-1]

	
s = "00"
print (decode(s))

