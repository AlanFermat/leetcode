from heapq import *
def findKth(nums, k):
	h = []
	for num in nums:
		heappush(h, -num)
	for _ in range(k-1):
		heappop(h)
	return -heappop(h)

nums = [3,2,3,1,2,4,5,5,6]
k = 4

print (findKth(nums, k))
	