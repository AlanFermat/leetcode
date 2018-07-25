def arrPairSum(nums):
	"""
	type: list 2n length
	rtype: int
	"""
	nums.sort()
	summ = 0
	for index in range(len(nums)/2):
		summ += nums[2*index]
	return summ



nums = [1,2,4,5,7,8]
print arrPairSum(nums)