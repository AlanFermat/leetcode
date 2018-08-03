def minCostClimbingStairs(cost):
	"""
	:type cost: List[int]
	:rtype: int
	"""
	S = {}
	S[1] = {}
	S[2] = {}
	S[1][-1] = cost[0]
	S[1][-2] = 0
	S[2][-1] = cost[1]
	S[2][-2] = cost[0]
	n = len(cost)
	if n == 2:
		return min(S[1][-1], S[2][-1])
	else:
		for i in range(n-2):
			S[1][i] = min(S[1][i-1], S[2][i-2]) + cost[i+1]
			S[2][i] = min(S[1][i-1], S[2][i-2]) + cost[i+2]
		S[1][n-2] = min(S[1][n-3],S[2][n-4]) + cost[n-1]
		k = min(S[1][n-2],S[2][n-3])
		p = min(S[1][n-3],S[2][n-4])
		return min(k,p)

c = [0,1,0,0]
print minCostClimbingStairs(c)