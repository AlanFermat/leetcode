from collections import defaultdict as dd
def canCross(stones):
	"""
	:type stones: List[int]
	:rtype: bool
	"""
	if stones[1] > 1:
		return False
	n = len(stones)
	# we will use a tabulation method here by recording the number of steps we are progressing at each jump
	# note that dp[stones[i]] is a list meaning how many steps we take from the previous spot to this spot 
	# on the next step we just try every possible steps from this current point and see how far we gonna get
	
	dp = dd(set)
	
	dp[0] = set([0])
	
	for i in range(n):
		for k in dp[stones[i]]:
			for step in [k-1,k,k+1]:
				nextStone = stones[i] + step
				if nextStone != stones[i]:
					dp[nextStone].add(step)
	return dp[stones[n-1]] != set()  

stones = [0,1,2,3,4,8,9,11]  
print (canCross(stones))