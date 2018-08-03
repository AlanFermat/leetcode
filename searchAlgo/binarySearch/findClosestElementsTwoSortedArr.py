import sys
def binaryFindClosest(seq, num1, start, end):
	"""
	Locate num1 in this sorted array seq
	by returning minimum distance between num1 and any element in seq
	O(logn)
	"""
	mid = (start + end)/2
	while end >= start:
		if seq[mid] == num1:
			return 0
		elif seq[mid] > num1:
			return binaryFindClosest(seq, num1, start, mid-1)
		else:
			return binaryFindClosest(seq, num1, mid+1, end)
	if mid < 0 :
		return abs(seq[0] - num1)
	if mid >= len(seq) -1:
		return abs(seq[len(seq)-1] - num1)
	return min(abs(seq[mid] - num1),abs(seq[mid+1] - num1))

			

# def findCloset(seq1,seq2):
#   """
#   O(n2) 
#   """
# 	minVal = sys.maxint
# 	for num1 in seq1:
# 		for num2 in seq2:
# 			ans = abs(num2-num1)
# 			if ans < minVal:
# 				minVal = ans
# 	return minVal
			

def findClosetOne(seq1, seq2):
	"""
	O(nlogn)
	"""
	minVal = sys.maxint
	for num1 in seq1:
		diff = binaryFindClosest(seq2,num1,0,len(seq2)-1)
		minVal = min(diff, minVal)
	return minVal

seq1 = [-2, 18, 30, 79, 199]
seq2 = [1, 12, 22, 24, 119]
print findClosetOne(seq1, seq2)



