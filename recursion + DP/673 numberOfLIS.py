def findNumberOfLIS(nums):
	if not nums:
		return 0
	n = len(nums)
	if n == 1:
		return n
	# wanna to install the length of the LIS uptil this point
	# and the number of LIS uptil this point
	dp = [[1,1] for _ in range(n)]
	longest = 1
	for j in range(n):
		latter = nums[j]
		curr_longest = 1
		count = 0
		for i in range(j):
			if nums[i] < latter:
				curr_longest = max(curr_longest, dp[i][0] + 1)
		for i in range(j):
			if nums[i] < latter and curr_longest == dp[i][0] + 1:
				count += dp[i][1]
		dp[j] = [curr_longest, max(count, dp[j][1])]
		longest = max(curr_longest, longest)
	total = sum([dp[i][1] for i in range(n) if dp[i][0] == longest])
	return total