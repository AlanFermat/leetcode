# def lengthOfLIS(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if not nums:
#         return 0
#     nums = [-float('inf')] + nums
#     n = len(nums)
	
#     # dp[i,j] stands for the length of LIS A j:n
#     # where each entry is larger than A[i]
#     dp = [[0 for _ in range(n+1)] for _ in range(n)]
	
#     for j in range(n-1,-1,-1):
#         for i in range(j):
#             if nums[j] <= nums[i]:
#                 dp[i][j] = dp[i][j+1]
#             else:
#                 dp[i][j] = max(dp[i][j+1], 1 + dp[j][j+1])
#     return dp[0][1]
def lengthOfLIS(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if not nums:
		return 0
	n = len(nums)
	dp = [0 for _ in range(n)]
	dp[0] = 1
	ans = 0
	for i in range(0,n):
		up_to_j = 0
		for j in range(i):
			## up_to_j record the LiS up to jth entry in the 
			## sequence
			if nums[i] >  nums[j]:
				up_to_j = max(up_to_j, dp[j])
		dp[i] = 1 + up_to_j
		ans = max(dp[i], ans)
	return ans
nums =[1,2,3,2]
print (lengthOfLIS(nums))

