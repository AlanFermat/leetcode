def encodeString(s):
	n = len(s)
	if n < 5:
		return s
	dp = [[[] for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(i,n):
			

