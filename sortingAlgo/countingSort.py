#a sorting technique based on keys between a specific range

RANGE_CONSTANT = 100
def countingSort(seq):
	"""
	O(n + k)
	where k is range of the seq
	"""
	count = [0] * RANGE_CONSTANT
	for item in seq:
		count[item] += 1
	for i in range(len(count)-1):
		count[i+1] += count[i]
	new_seq = [-1] * len(seq)
	for j in range(len(seq)):
		new_seq[count[seq[j]-1]] = seq[j]
		count[seq[j]-1] -= 1
	return new_seq

seq = [9,10,28,16,15,17,8,5]
print countingSort(seq)