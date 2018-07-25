from math import sqrt
from time import time
#http://www.geeksforgeeks.org/jump-search/
def jumpSearch(seq, start, end, num):
	"""
	STEP 1: Jump from index 0 to index 4;
	STEP 2: Jump from index 4 to index 8;
	STEP 3: Jump from index 8 to index 16;
	STEP 4: Since the element at index 16 is greater than 55 we will jump back a step to come to index 9.
	
	"""
	n = len(seq)
	m = int(sqrt(end-start))
	while start < n:
		if seq[start] == num:
			return start
		elif seq[start] < num:
			start += m
		else:
			end = start+1
			start = end - m
			return jumpSearch(seq, start, end, num)
	return -1



t1 = time()

seq = range(100000000)
num = 55
result = jumpSearch(seq, 0, len(seq)-1, num)

t2 = time()
print str(t2-t1)
print result

