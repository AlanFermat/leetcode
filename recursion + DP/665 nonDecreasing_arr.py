def isNon(arr):
	for i in xrange(len(arr)-1):
		if arr[i] > arr[i+1]:
			return False
	return True

def ifNonDecreasing(arr):
	n = len(arr)
	seq1 = arr[:]
	seq2 = arr[:]
	for i in range(n-1):
		if arr[i] > arr[i+1]:
			seq1[i] = seq1[i+1]
			seq2[i+1] = seq2[i]
			return isNon(seq1) or isNon(seq2)
	return True


arr = [3,5,3,4]
print ifNonDecreasing(arr)
			