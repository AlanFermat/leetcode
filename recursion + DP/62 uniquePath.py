def uniquePath(m,n):
	S = {}
	for i in range(1,m+1):
		S[i] = {}
		S[i][1] = 1
	for i in range(1,n+1):
		S[1][i]= 1
	for i in range(2,m+1):
		for j in range(2,n+1):
			S[i][j] = S[i-1][j] + S[i][j-1]
	return S[m][n]

m = 7
n = 3
print uniquePath(m,n)
