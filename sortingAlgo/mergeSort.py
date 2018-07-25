from time import time
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


# notice that merge will take O(n) time 
# while split them up will take log(n)

def merge(seq,l,m,r):
	"""
	Merge two sequences in the ascending order
	"""
	l1 = m - l +1
	l2 = r - m
	temp1 = [0] * l1
	temp2 = [0] * l2
	for idx1 in range(l1):
		temp1[idx1] = seq[idx1+l]

	for idx2 in range(l2):
		temp2[idx2] = seq[m+1+idx2]

	i = 0
	j = 0
	k = l
	# add to the seq and exhaust one of the i, j
	while i < l1 and j < l2:
		if temp1[i] < temp2[j]:
			seq[k] = temp1[i]
			i += 1
		else:
			seq[k] = temp2[j]
			j += 1
		k += 1
	# add additional items to the seq
	while i < l1:
		seq[k] = temp1[i]
		i += 1
		k += 1
	while j < l2:
		seq[k] = temp2[j]
		j += 1
		k += 1



def mergeSort(seq, l ,r):
	"""
	O (nlogn)
	"""
	if r > l:
		m = (l+(r-1))/2
		mergeSort(seq, l, m)
		mergeSort(seq, m+1,r)
		merge(seq, l ,m, r)
	return seq


t1 = time()
seq = range(1000001)
seq = mergeSort(seq, 0, 1000000)

t2 = time()

print t2 -t1


