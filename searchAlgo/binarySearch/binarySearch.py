# This is for sorted array only
# Recursion form
#http://www.geeksforgeeks.org/binary-search/
from time import time

def binarySearch(seq,start, end,num):
	if end >= start:
		middle = start + (end-start)//2
		if seq[middle] == num:
			return middle
		elif seq[middle] < num:
			return binarySearch(seq, middle+1, end, num)
		else:
			return binarySearch(seq, start, middle-1, num)
	else:
		return -1


# Iteration form
def binarySearchIte(seq, start, end, num):
	while end >= start:
		middle = start + (end -start)//2
		if seq[middle] == num:
			return middle
		elif seq[middle] < num:
			start = middle +1
		else:
			end = middle -1
	return -1

# Test 
# t1 = time()
# seq = range(50000000)
# num = 55
# start, end = 0, len(seq)-1
# result = binarySearchIte(seq, start, end, num)
# t2 = time()

# print str(t2-t1)
# print result

