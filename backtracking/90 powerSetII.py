def powerSets(s):
	res = [[]]
	nums = sorted(nums)
	for num in nums:
		for j in range(len(res)):
			if [num] + res[j] not in res:
				res.append([num] + res[j])
	return res