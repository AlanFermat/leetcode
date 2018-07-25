def tripletsZeroSum(seq):
	"""
	return all triplets with summation 0
	O(n2) solution
	"""
	result = []
	for i in range(len(seq)-1):
		mapp = []
		for j in range(i+1,len(seq)):
			summ = seq[i] + seq[j]
			if (-summ) in mapp:
				result.append((seq[i], seq[j], -summ))
			else:
				mapp.append(seq[j])
	return result

seq= [0, -1, 2, -3, 1]
print tripletsZeroSum(seq)