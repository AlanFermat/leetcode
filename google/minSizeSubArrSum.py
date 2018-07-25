def minSubArrayLen(s, nums):
	
	if not nums:
		return 0
	i, j = 0, 0
	currSum = 0
	minLen = len(nums) + 1

	while j < len(nums):        
		
		while j < len(nums) and currSum < s:
			currSum += nums[j]
			j += 1
		while i < j and currSum >= s:
			currSum -= nums[i]
			i += 1
		minLen = min(minLen, j - i + 1)
		
	return minLen if minLen <= len(nums) else 0
nums = [1,2,3,4,5]
s = 0

print (minSubArrayLen(s, nums))