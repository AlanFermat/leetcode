def maxSubArrayLen(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	if not nums:
		return 0
	d = {}
	n = len(nums)
	idx = 0
	summ = 0
	while idx < n:
		summ += nums[idx]
		d[summ] = d.get(summ,[]) + [idx]
		idx += 1
	print (d)
	candidate = []
	if k in d:
		candidate.append(max(d[k])+1)
	for key in d:
		if key - k in d and max(d[key]) > min(d[key-k]):
			candidate.append(max(d[key]) - min(d[key-k]))
	print (candidate)
	if candidate:
		return max(candidate)
	return 0

nums = [1,-1,5,3,-2,3,0,0,0,-1,0]
k = 3
print (maxSubArrayLen(nums,k))
