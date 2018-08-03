def uniquePath(arr):
	S = {}
	m = len(arr)
	n = len(arr[0])
	S[0] = {}
	S[0][1] = 1
	for i in range(1,m+1):
		S[i] = {}
		if arr[i-1][0] == 1 or S[i-1][1] == 0:
			S[i][1] = 0
		else:
			S[i][1] = 1
	S[1][0] = 1
	for j in range(1,n+1):
		if arr[0][j-1] == 1 or S[1][j-1] == 0:
			S[1][j] = 0
		else:
			S[1][j] = 1
	for i in range(2,m+1):
		for j in range(2,n+1):
			if arr[i-1][j-1] == 0:
				S[i][j] = S[i-1][j] + S[i][j-1]
			else:
				S[i][j] = 0
	return S[m][n]



arr = [[0,0,0],[0,1,0],[0,0,0]]
print uniquePath(arr)
