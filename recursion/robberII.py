def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if not nums:
		return 0
	if len(nums) == 1:
		return nums[0]
	rob_first, rob_last = 0, 0
	# greedy
	prev= 0
	for num in nums[1:]:
		temp = rob_first
		rob_first  = max(rob_first, prev + num)
		prev = temp
		print (rob_first , prev)
		
	prev= 0
	for num in nums[:-1]:
		rob_last, prev = max(rob_last, prev + num), rob_last
	return max(rob_first, rob_last)

nums = [2,4,1,1,7]
print (rob(nums))