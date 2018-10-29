# no requirement for relative order
# def moveZero(nums):
# 	n = len(nums)
# 	i, j = 0, n - 1
# 	while i < j:
# 		while i < j and nums[j] == 0:
# 			j -= 1
# 		if i == j:
# 			break
# 		if not nums[i]:
# 			nums[i], nums[j] = nums[j], nums[i]
# 			i += 1
# 			j -= 1
# 			continue
# 		i += 1

def moveZeroOrder(nums):
	n = len(nums)
	i, j = 0, 1
	while i < n and j < n:
		if not nums[i] and nums[j]:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j += 1
		elif nums[i] and not nums[j]:
			i, j = j, j+1
		else:
			j += 1


nums = [10,2,4,8]
moveZeroOrder(nums)
print (nums)