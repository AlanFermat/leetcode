#http://www.geeksforgeeks.org/fibonacci-search/
# # Similarities with Binary Search:

# # Works for sorted arrays
# # A Divide and Conquer Algorithm.
# # Has Log n time complexity.
# # Differences with Binary Search:

# # Fibonacci Search divides given array in unequal parts
# # Binary Search uses division operator to divide range. 
# # The division operator may be costly on some CPUs.
# # Fibonacci Search examines relatively closer elements in subsequent steps. 
# # So when input array is big that cannot fit in CPU cache or even in RAM, Fibonacci Search can be useful.

# ALGORITHM
# Let arr[0..n-1] be the input array and element to be searched be x.

# Find the smallest Fibonacci Number greater than or equal n. 
# Let this number be fibM mth Fibonacci Number. Let the two Fibonacci numbers preceding 
# it be fibMm1 (m-1)th Fibonacci Number and fibMm2 (m-2)th Fibonacci Number.
# While the array has elements to be inspected:
# Compare x with the last element of the range covered by fibMm2
# If x matches, return index
# Else If x is less than the element, move the three Fibonacci variables two Fibonacci down, 
# indicating elimination of approximately rear two-third of the remaining array.
# Else x is greater than the element, move the three Fibonacci variables one Fibonacci down. 
# Reset offset to index. Together these indicate elimination of approximately 
# front one-third of the remaining array.
# Since there might be a single element remaining for comparison, check if fibMm1 is 1. 
# If Yes, compare x with that remaining element. If match, return index.

from time import time
def findFibo(n):
	a = 0
	b = 1
	c = a + b
	while c < n:
		a = b
		b = c
		c = a + b
	return c,b,a

# print findFibo(10)


def fibonacciSearch(seq, num):
	if len(seq) == 1 and seq[0] == num:
		return 0
	fibMm, fibMm1, fibMm2 = findFibo(len(seq))
	start = -1
	# The first time we locate at fibMm2 - 1 th position in the seq
	while fibMm1 > 1:
		index = min (fibMm2 + start, len(seq) - 1)
		if seq[index] == num:
			return index
		elif seq[index] > num:
			fibMm, fibMm1, fibMm2 = findFibo(fibMm2)
		else:
			start = index
			fibMm, fibMm1, fibMm2 = findFibo(fibMm1)
	index = start + fibMm1 
	if fibMm1 == 1 and seq[index] == num:
		return index
	return -1

t1 = time()
seq  = range(100000000)
num = 100
result = fibonacciSearch(seq, num)
t2 = time()
print str(t2 - t1)
print result




	