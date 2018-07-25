seq = [4,3,5,2,2,6]

def findRepeatMissingSort(seq):
	"""
	O(nlogn)
	"""
	seq.sort()
	output = []
	for i in range(len(seq)-1):
		if seq[i] == seq[i+1]:
			output.append(seq[i])
		if seq[i+1] - seq[i] > 1:
			output.append(seq[i] + 1)
	return output


def countArrMethod(seq):
	"""
	O(n )
	"""
	count = [0] * (len(seq))
	for item in seq:
		count[item-1] += 1
	output = [count.index(0)+1, count.index(2)+1]
	return output


print countArrMethod(seq)

			