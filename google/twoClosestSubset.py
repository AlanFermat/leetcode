from collections import defaultdict as dd
def sol(arr):
	diff = float("inf")
	total = sum(arr)
	n = len(arr)
	dp = [[False for _ in range(total + 1)] for _ in range(n + 1)] 
	for i in range(n+1):
		dp[i][0] = True
	for i in range(1, total + 1):
		dp[0][i] = False
	for i in range(1,n+1):
		for j in range(1,total+1):
			dp[i][j] = dp[i-1][j]
			if arr[i-1] <= j:
				dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
	for j in range(total//2, -1, -1):
		if dp[n][j]:
			diff = total - 2 * j
			break
	return diff

arr = [3,4,5,1,3,6]


print (sol(arr))
				
