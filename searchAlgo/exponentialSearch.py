#http://www.geeksforgeeks.org/exponential-search/
# Idea: find the subarray by exponentially 
# trying the starting point and ending point
# then do the binary search
from time import time
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

def exponentialSearch(seq, num):
	start = 0
	end = 1
	while seq[end] < num:
		start = end
		end *= 2
	if seq[end] == num:
		return end
	else:
		return binarySearchIte(seq, start, end, num)
	return -1


t1 = time()
seq = range(10000000)
num = 55
start, end = 0, len(seq)-1
result = exponentialSearch(seq, num)
t2 = time()

print str(t2-t1)
print result
