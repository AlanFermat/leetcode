"""
	Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
	Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums or len(nums) == 1:
			return 0
		n = len(nums)
		
		##### dp[i] stands for the minimum steps to get to the index i
		
# O(n^2)
#         dp = [float("inf") for _ in range(n)]
#         dp[0]= 0
#         for i in range(n-1):
#             for j in range(nums[i], 0, -1):
#                 if i + j < n:
#                     if dp[i+j] > dp[i] + 1:
#                         dp[i+j] = dp[i] + 1
#                     else:
#                         break
					
#         return dp[n-1]  


		#### greedy, each step choose the one that will get the furthest
		start, end = 0, 0
		ans = 0
		while end < n - 1:
			largest = end
			for i in range(start, end+1):
				largest = max(largest, i + nums[i])
			start = end + 1
			end = largest
			ans += 1
			if ans == n-1:
				break
		return ans

			


s = Solution()
nums = [1,1,1,0,0]
print (s.jump(nums))

		

		
				
		
		
		