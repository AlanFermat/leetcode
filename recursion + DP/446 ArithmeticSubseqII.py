from collections import defaultdict as dd
def numberOfArithmeticSlices(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	if not A:
		return 0
	n = len(A)
	dp = [dd(int) for _ in range(n)]
	length2 = 0
	res = 0
	for i in range(1,n):
		for j in range(i-1, -1, -1):
			diff = A[i] - A[j]
			dp[i][diff] += 1
			length2 += 1
			if diff in dp[j]:
				dp[i][diff] += dp[j][diff]
		res += sum(dp[i].values())
	return res - length2
				
			