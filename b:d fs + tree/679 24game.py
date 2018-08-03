def judgePoint24(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	if len(nums) == 1:
		return abs(nums[0] - 24.0) < 0.1
	else:
		for i in range(len(nums)):
			for j in range(len(nums)):
				temp = []
				num_del = []
				if i != j:
					indices = list(range(len(nums)))
					indices.remove(i)
					indices.remove(j)
					temp.append(nums[i]+nums[j])
					temp.append(nums[i] - nums[j])
					temp.append(nums[j] - nums[i])
					temp.append(nums[i] * nums[j])
					if nums[i] != 0:
						temp.append(float(nums[j]/float(nums[i])))
					if nums[j] != 0:
						temp.append(float(nums[i]/float(nums[j])))
					for k in indices:
						if k != i and k != j:
							num_del.append(nums[k])
					for x in temp:
						if judgePoint24(num_del + [x]):
							return True
				else:
					continue
		return False

nums = [1,9,3,2]
print (judgePoint24(nums))

