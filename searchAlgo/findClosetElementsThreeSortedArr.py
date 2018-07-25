#Given three sorted arrays A[], B[] and C[], 
#find 3 elements i, j and k from A, B and C respectively 
#such that max(difference)is minimized. Here abs() indicates absolute value.
import sys
# def findClosest(seq1,seq2, seq3):
# 	"""
# 	O(n3)
# 	"""
# 	minVal = sys.maxint
# 	for num1 in seq1:
# 		for num2 in seq2:
# 			for num3 in seq3:
# 				if max(abs(num1-num2),abs(num1-num3),abs(num3-num2)) < minVal:
# 					minVal = max(abs(num1-num2),abs(num1-num3),abs(num3-num2))
# 					ans = [num1, num2, num3]
# 	return ans



def binaryFindClosest(seq, num1, start, end):
	"""
	Locate num1 in this sorted array seq
	by returning minimum distance between num1 and any element in seq
	O(logn)
	"""
	mid = (start + end)/2
	while end >= start:
		if seq[mid] == num1:
			return mid
		elif seq[mid] > num1:
			return binaryFindClosest(seq, num1, start, mid-1)
		else:
			return binaryFindClosest(seq, num1, mid+1, end)
	if mid < 0 :
		return 0
	if mid >= len(seq) -1:
		return len(seq)-1
	return mid

def result(minVal, seq1,seq2,seq3):
	for num1 in seq1:
		ind2 = binaryFindClosest(seq2, num1, 0, len(seq2)-1)
		ind3 = binaryFindClosest(seq3, num1, 0, len(seq3)-1)
		num2 = seq2[ind2]
		num3 = seq3[ind3]
		val1 = max(abs(num1-num2),abs(num1-num3),abs(num3-num2))
		if val1 < minVal:
			minVal = val1
			ans1 = [num1, num2, num3, minVal] 
	return ans1


def findClosestOne(seq1,seq2,seq3):
	minVal = sys.maxint
	ans1 = result(minVal, seq1, seq2, seq3)
	ans2 = result(minVal, seq2, seq1, seq3)
	ans3 = result(minVal, seq3, seq2, seq1)
	return ans1, ans2, ans3



seq1 = [1, 4, 10]
seq2 = [2, 15, 20]
seq3 = [10, 12]
print findClosestOne(seq1, seq2, seq3)


