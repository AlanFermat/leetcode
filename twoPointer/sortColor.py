def sortColor(nums):
	n = len(nums)
	count0 =0
	count1 =0
	for i in range(n):
		if nums[i] == 0:
			count0 += 1
		if nums[i] == 1:
			count1 += 1
	print count0, count1
	for j in xrange(n):
		if j < count0:
			nums[j] = 0
		if count0 <= j < count0 + count1:
			nums[j] =1
		if j >= count1 + count0:
			nums[j] = 2

	
			
			


nums = [0,2,0,2,2,2,0,0,0,0,0,0,0,2,2,0]
print len(nums), nums
sortColor(nums)
print len(nums),nums