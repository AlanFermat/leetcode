from binarySearch import binarySearch
#http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

seq = [6, 7, 8, 9, 10, 1, 2, 3, 4,5]
num = 3


def findPivot(seq, lo, hi):
	if lo == hi:
		return hi
	if lo > hi:
		return -1
	middle = (lo + hi) /2
	if seq[middle] > seq[middle + 1] and middle > lo:
		return middle
	if seq[middle] < seq[middle-1] and middle < hi:
		return middle -1
	if seq[middle] <= seq[hi]:
		return findPivot(seq, lo, middle - 1)
	return findPivot(seq, middle+1, hi)

def rotateFinding(seq, num):
	lo = 0
	hi = len(seq)-1
	pivot = findPivot(seq, lo, hi)
	if pivot == -1:
		return binarySearch(seq, lo, hi, num)
	elif seq [pivot] == num:
		return pivot
	elif seq [0] < num:
		return binarySearch(seq, lo, pivot, num)
	return binarySearch(seq, pivot + 1, hi, num)

print rotateFinding(seq, num)


	



