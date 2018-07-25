#http://www.geeksforgeeks.org/interpolation-search/
# Only for sorted array
# where the values in a sorted array are uniformly distributed
# // The idea of formula is to return higher value of pos
# // when element to be searched is closer to arr[hi]. And
# // smaller value when closer to arr[lo]
# pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]
from time import time
def interpolationSearch(seq, num):
	"""
	Step1: In a loop, calculate the value of pos using the probe position formula.
	Step2: If it is a match, return the index of the item, and exit.
	Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array. Otherwise calculate the same in the right sub-array.
	Step4: Repeat until a match is found or the sub-array reduces to zero.
	"""
	lo = 0
	hi = len(seq) -1
	while lo <= hi and num >= seq[lo] and num <= seq[hi]:
		pos = lo + int(((num-seq[lo])*float(hi-lo) / (seq[hi]-seq[lo])))
		if seq[pos] == num:
			return pos
		elif seq[pos] < num:
			lo = pos + 1
		else:
			hi = pos - 1
	return -1


t1 = time()
seq = range(50000000)
num = 54
result = interpolationSearch(seq, num)
t2 = time()

print result
print str(t2-t1)
