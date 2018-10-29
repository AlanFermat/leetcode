from random import *

def kth(lst, k):
	findKthSmallest(lst, k, 0, len(lst) - 1)


def findKthSmallest(lst,k,left, right):
	if k >=0 and k <= right - left + 1:
		pos = partitionRandom(lst, left, right)
		if pos - left == k:
			return lst[pos]
		if pos - left > k:
			print ("ss")
			return findKthSmallest(lst, left, pos-1,k)
		return findKthSmallest(lst, pos+1,right,k-pos+left-1)
	return 0

def partitionRandom(lst, left, right):
	pivot = randint(left, right)
	swap(lst, left + pivot, right)
	return partition(lst, left, right)

def partition(nums, l, r):
	x = nums[r]
	i = l
	for j in range(l, r):
		if nums[j] <= x:
			swap(nums, i, j)
			i += 1
	swap(nums, i, r)
	return i

def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]


lst = [1,2,3,2,4,5]
k = 2
print (kth(lst, k))