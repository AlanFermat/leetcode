def findMedian(seq):
	if len(seq) % 2 == 0:
		return (seq[len(seq)/2] + seq[len(seq)/2-1])/2.0
	return seq[len(seq)/2]




def simpleMedian(seq1,seq2):
	s = seq1 + seq2
	s.sort()
	return findMedian(s)
	

def medianTwoSortedList(seq1, seq2):
	n = len(seq1) # this is for the case when two sequences are of the same length
	if seq1 == []:
		return findMedian(seq2)
	if seq2 == []:
		return findMedian(seq1)
	if len(seq1) <= 2 and len(seq2) <= 2:
		return simpleMedian(seq1, seq2)
	am = findMedian(seq1)
	bm = findMedian(seq2)
	if am == bm:
		return am
	elif am < bm:
		if n % 2:
			return medianTwoSortedList(seq1[len(seq1)/2:], seq2[:len(seq2)/2+1])
		return medianTwoSortedList(seq1[len(seq1)/2:], seq2[:len(seq2)/2])
	elif am > bm:
		if n % 2:
			return medianTwoSortedList(seq1[:len(seq1)/2+1], seq2[len(seq2)/2:])
		return medianTwoSortedList(seq1[:len(seq1)/2], seq2[len(seq2)/2:])
	return -1

		




seq1 = [1, 12, 15, 26, 38]
seq2 = [2, 13, 16, 30, 45]
print medianTwoSortedList(seq1, seq2)