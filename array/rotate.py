def rotate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	new = nums[-k:] + nums[:-k]
	for i in range(len(nums)):
		nums[i] = new[i]

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)
print (nums)