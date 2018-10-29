def checkSubarraySum(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	for num in nums:
		if num == k:
			return True
	summation = 0
	sum_map = {0:-1}
	for i in range(len(nums)):
		summation += nums[i]
		rem = summation - k
		if sum_map.get(rem, -2) != -2:
			if i - sum_map[rem] > 1:
				return True
		else:
			sum_map[summation] = i
	return False

nums = [-3,1,-4,-1,3,2,1]
k = sum(nums)
print (checkSubarraySum(nums, k))