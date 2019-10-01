def majorityElement(nums):
	if not nums:
		return ""
	count = 1
	res = nums[0]
	for i in range(1, len(nums)):
		var = nums[i]
		if count == 0:
			res = var
		else:
			if var != res:
				count -= 1
			else:
				count += 1
	return res


nums = [3,2,4,3,3,4,4,3,4,4]

print (majorityElement(nums))