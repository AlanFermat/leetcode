def find3Sum(nums, target):
	res = []
	if len(nums) < 3:
		return []
	if len(nums) == 3:
		if sum(nums) == target:
			return [nums]
		else:
			return res
	nums = sorted(nums)
	print (nums)
	for i in range(len(nums) - 2):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		j, k = i+1, len(nums)-1
		new_target = target - nums[i]
		while j < k:
			if nums[j] + nums[k] == new_target:
				res.append([nums[i], nums[j], nums[k]])
				while j < k and nums[j] == nums[j+1]:
					j += 1
				k -= 1
			elif nums[j] + nums[k] > new_target:
				k -= 1
			elif nums[j] + nums[k] < new_target:
				j += 1
	return res


def find3SumDuplicate(nums, target):
	# res = []
	cnt = 0
	if len(nums) < 3:
		return 0
	if len(nums) == 3:
		if sum(nums) == target:
			return 1
		else:
			return 0
	nums = sorted(nums)
	print (nums)
	for i in range(len(nums) - 2):
		j, k = i+1, len(nums)-1
		new_target = target - nums[i]
		while j < k:
			if nums[j] + nums[k] == new_target:
				if nums[j] != nums[k]:
					# therefore, for max j, it can only be that 
					# j = k-1
					left = right = 1
					while j + 1 < k and nums[j] == nums[j+1]:
						j += 1
						left += 1
					while k > j + 1 and nums[k] == nums[k-1]:
						k -= 1
						right += 1
					cnt += left * right
					j += 1
					k -= 1
				else:
					cnt += (k-j+1) * (k-j) // 2
					break

			elif nums[j] + nums[k] > new_target:
				k -= 1
			elif nums[j] + nums[k] < new_target:
				j += 1
	return cnt




A = [1,1,2,2,4,4,3,3,5,5]
target = 8

# nums = [-4,-4,-1,0,7,7,7]
# target = 3

print (find3SumDuplicate(A, target))

