from bisect import *
def countSmaller(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	if not nums:
		return []
	if len(nums) == 1:
		return [0]
	l, r= nums[:len(nums)//2], nums[len(nums)//2:]
	left = self.countSmaller(l)
	right = self.countSmaller(r)
	r_sorted = sorted(r)
	for i in range(len(left)):
		left[i] += bisect_left(r_sorted, l[i])
	return left + right

a = [1,2,3,4,5]
print (bisect_right(a,2))