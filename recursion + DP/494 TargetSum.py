from collections import defaultdict as dd
def findTargetSumWays(nums, S):
	"""
	:type nums: List[int]
	:type S: int
	:rtype: int
	"""
	dp = dd(int)
	dp[0]= 1
	# dp[k] stores number of possible ways to get sum k
	for num in nums:
		new = dd(int)
		for k, v in dp.items():
			new[k+num] += v
			new[k-num] += v
		dp = new
	return dp[S]

nums = [1,1,1,1,1]
S = 3
print findTargetSumWays(nums, S)