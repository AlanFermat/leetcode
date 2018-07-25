#http://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/
import sys
def smallestAndSecondSmallest(seq):
	"""
	Find smallest and Second Smallest element in an array
	O(n)
	"""
	first = second = sys.maxint
	for element in seq:
		if element < first:
			second = first
			first = element
		elif element < second:
			second = element
	return first, second


seq = [1,22,3,4,3,9,7,10]
print smallestAndSecondSmallest(seq)
			


