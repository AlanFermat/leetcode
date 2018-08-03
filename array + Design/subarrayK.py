def subarraySum(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	s = {0:1}
	n = len(nums)
	count = 0
	summation = 0
	for i in range(n):
		summation += nums[i]
		if summation - k in s:
			count += s[summation - k]
		s[summation]= s.get(summation, 0) + 1
	return count

nums = [1]
k = 0
print subarraySum(nums, k)