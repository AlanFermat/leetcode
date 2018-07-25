def generate(nums):
	n = len(nums)
	gen = []
	if n == 0:
		return [[]]
	else:
		for i in range(n):
			p = nums[i]
			nums[0],nums[i] = nums[i],nums[0]
			k = generate(nums[1:])
			gen += [[p] + x for x in k]
		return gen


nums = []
print generate(nums)