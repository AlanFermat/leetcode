def reshapeMat(nums,r,c):
	row = len(nums)
	column = len(nums[0])
	storage = []
	ans = []
	start = 0
	if row * column != r * c:
		return nums
	else:
		for i in range(len(nums)):
			for j in range(len(nums[0])):
				storage.append(nums[i][j])
		for index in range(len(storage)):
			if (index+1)%c == 0:
				ans.append(storage[start:start+c])
				start = start+c
	return ans



nums = [[1,2],[3,4]]
r = 4
c = 1
print reshapeMat(nums,r,c)