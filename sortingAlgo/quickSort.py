from random import randint
from time import time

def partition(seq, lo, hi):
	"""
	Swap the pivot so that the pivot element will finally be located
	at the right position with the index i+1
	Left of the pivot is smaller than or equal to pivot
	Right of the pivto is larger than the pivot
	"""
	pivot_index = hi
	pivot = seq[pivot_index]
	i = lo-1
	for j in range(lo,hi):
		if seq[j] <= pivot:
			i += 1
			seq[i], seq[j] = seq[j], seq[i]
	seq[i+1], seq[hi]=seq[hi], seq[i+1] 
	return i + 1
		
	



def quickSort(seq, lo, hi):
	if lo < hi:
		# pivot = randint(lo, hi)
		# temp = seq[hi]
		# seq[hi] = seq[pivot]
		# seq[pivot] = temp
		#position of the pivot
		pos = partition(seq, lo, hi)
		quickSort(seq, lo, pos-1)
		quickSort(seq, pos, hi)


seq= [123300,2,1,111,22,92,4,6,9,1,2,3,4,2,11111111]
quickSort(seq,0,len(seq)-1)
print seq