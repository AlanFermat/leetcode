##### O(n^2) both time and space
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


##### O(n^2) time O(n) space
# def lengthOfLIS(nums):
# 	"""
# 	:type nums: List[int]
# 	:rtype: int
# 	"""
# 	if not nums:
# 		return 0
# 	n = len(nums)
# 	dp = [0 for _ in range(n)]
# 	dp[0] = 1
# 	ans = 0
# 	for i in range(0,n):
# 		up_to_j = 0
# 		for j in range(i):
# 			## up_to_j record the LiS up to jth entry in the 
# 			## sequence
# 			if nums[i] >  nums[j]:
# 				up_to_j = max(up_to_j, dp[j])
# 		dp[i] = 1 + up_to_j
# 		ans = max(dp[i], ans)
	# return ans

##### O(nlog(n)) time O(n) space


"""
seq is the input sequence.

L is a number: it gets updated while looping over the sequence and 
it marks the length of longest incresing subsequence found up to that moment.

M is a list. M[j-1] will point to an index of seq that holds the smallest 
value that could be used (at the end) to build an increasing subsequence of length j.

P is a list. P[i] will point to M[j], where i is the index of seq. 
In a few words, it tells which is the previous element of the subsequence. 
P is used to build the result at the end.

"""
def LIS(nums):
	if not nums:
		return nums
	n = len(nums)
	M = [None] * n
	P = [None] * n
	L = 1
	M[0] = 0
	for i in range(1,n):

		# Binary search: we want the largest j <= L
		#  such that seq[M[j]] < seq[i] (default j = 0),
		#  hence we want the lower bound at the end of the search process.
		upper, lower = L, 0

		# Since the binary search will not look at the upper bound value,
		# we'll have to check that manually
		if nums[M[upper-1]] < nums[i]:
			j = upper
		else:
			while upper > lower + 1:
				mid = (upper + lower) //2
				if nums[M[mid-1]] >= nums[i]:
					upper = mid
				else:
					lower = mid
			
			j = lower

		P[i] = M[j-1]

		# adjust so that the last number in sequence is the smaller one
		if j == L or nums[i] < nums[M[j]]:
			M[j] = i
			L = max(L, j+1)
		# result = []
		# pos = M[L-1]
		# for _ in range(L):
		# 	result.append(nums[pos])
		# 	pos = P[pos]
	return L
			








nums =[3,-1,4]
print (LIS(nums))

