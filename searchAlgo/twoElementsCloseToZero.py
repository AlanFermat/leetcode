def twoSumCloseToZero(seq):
	"""
	Find a pair whose sum is closet to zero
	"""
	seq.sort()
	n = len(seq)
	start = 0 
	end = n - 1
	abs_sum = {}
	while start < end:
		value = seq[start] + seq[end]
		if abs(value) in abs_sum.keys():
			abs_sum[abs(value)] += [seq[start],seq[end]]
		if abs(value) not in abs_sum.keys():
			abs_sum[abs(value)] = [seq[start],seq[end]]
		if value == 0:
			break
		elif value < 0:
			start += 1
		else:
			end -= 1
	return abs_sum[min(abs_sum.keys())]


seq = [1, 60, -10, 70, -80, 85, 60, -10, 70, -80, 85]
print twoSumCloseToZero(seq)

		