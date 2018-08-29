def threeSumClosest(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	n = len(nums)
	if n < 3:
		return None
	elif n == 3:
		return sum(nums)
	else:
		nums.sort()
		min_d = float('inf')
		summ = float('inf')
		for i in range(0, n-2):
			j,k = i + 1, n-1
			while j < k:
				ttl = nums[i] + nums[j] + nums[k]
				diff = ttl - target
				if diff > 0:
					k -= 1
					if diff < min_d:
						summ = ttl
						min_d = diff
				elif diff<0:
					j += 1
					if abs(diff) < min_d:
						summ = ttl
						min_d = abs(diff)
				else:
					summ = ttl
					return summ
		return summ

nums = [1,1,1,0]
target = 100
print threeSumClosest(nums, target)
							
		