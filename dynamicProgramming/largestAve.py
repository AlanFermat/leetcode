from collections import *
def largestAve(arr,k):
	"""
		Give the largest average among
		all possible k-groups
	"""
	n = len(arr)
	if k <= 1:
		return sum(arr)*1.0/n
	elif k >= len(arr):
		return sum(arr)*1.0
	else:
		S = {}
		for i in range(1,n+1):
			S[i] = defaultdict(float)
			S[i][1] = 1.0 * sum(arr[:i])/i
		for p in range(2,k+1):
			for i in range(p,n+1):
				for j in range(p-1,i):
					S[i][p] = max(S[i][p], S[j][p-1] + sum(arr[j:i])*1.0 / (i-j))
		return S[n][k]

A = [1,2,3,4,5,6,7]
K = 4
print largestAve(A,K)
		
