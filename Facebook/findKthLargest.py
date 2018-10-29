def findKthLargest(nums, k):
	mid = partition(nums)
	if mid==k-1:
		return nums[mid]
	if mid>k-1:
		return findKthLargest(nums[:mid], k)
	else:
		return findKthLargest(nums[mid+1:], k-mid-1)

def partition(nums):
	if len(nums) <= 1:
		return 0
	i, j =0, len(nums) - 1
	nums[(i+j)//2], nums[0] = nums[0], nums[(i+j)//2]
	t = nums[i]
	while i < j:
		while i < j and nums[j] <= t:
			j -= 1
		if i < j:
			nums[i] = nums[j]
		while i < j and nums[i] >= t:
			i += 1

		if i<j:
			nums[j] = nums[i]
	nums[i] = t
	return i

