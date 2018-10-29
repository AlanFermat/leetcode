def subsetSum(nums, k):
	dp = [[False for _ in range(k+1)] for _ in range(len(nums))]
	for i in range(len(nums)):
		dp[i][0] = True

	# for j in range(1,k+1):
	# 	dp[0][j] = False

	for i in range(len(nums)):
		for t in range(1,k+1):
			if nums[i] <= t:
				# print (dp[i][t-nums[i]])
				dp[i][t] = dp[i-1][t] or dp[i-1][t-nums[i]]
			else:
				dp[i][t] = dp[i-1][t]
	print (dp[len(nums)-1][k])


def subsetSumSize(nums, k):
	dp = [[float("inf") for _ in range(k+1)] for _ in range(len(nums))]
	for i in range(len(nums)):
		dp[i][0] = 0
		if nums[i] <= k:
			dp[i][nums[i]] = 1
	for i in range(len(nums)):
		for t in range(1, k+1):
			if nums[i] <= t:
				dp[i][t] = min(dp[i-1][t], dp[i-1][t-nums[i]]+1)
			else:
				dp[i][t] = dp[i-1][t]
	print (dp[len(nums)-1][k])

nums = [2,3,8,7,10,2,4,4,4]
k = 44
subsetSumSize(nums, k)
	

