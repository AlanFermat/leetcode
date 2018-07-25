def threeSum(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	res = []
	n = len(nums)
	if n < 3:
		return []
	if n == 3:
		if sum(nums) == 0:
			return [nums]
		else:
			return []
	nums = sorted(nums)
	for k in range(n-2):
		if k > 0 and nums[k] == nums[k-1]:
			continue
		i,j = k+1, n-1
		ans = -nums[k]
		while i < j:
			if nums[i] + nums[j] == ans:
				res.append([nums[k], nums[i],nums[j]])
				idx1 = i
				while i < j and nums[idx1] == nums[i]:
					i += 1
				j -= 1
			if nums[i] + nums[j] > ans:
				j -= 1
			if nums[i] + nums[j] < ans:
				i += 1
	return res

nums = [-1, 0, 1, 2, -1, -4,2,-4]
print (threeSum(nums))

