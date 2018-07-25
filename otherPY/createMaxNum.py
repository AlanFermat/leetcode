# Recipe:
#	Step 1: Split the problem to find 2 sequences of digits separately from nums1
#			and nums2, one for length i another k-i
#   Step 2: Find the largest number in nums1 denote it as above, and the largest in nums2 as below
#	Step 3: We use the function maxSelectDigit to do Step 2 and return a list of sequence representing 
#           largest possible
#   Step 4: We merge two lists to find the maximum final result using function mergeTwoSeq
#	Step 5: Finally we iterate over all possible choices for the length of above and below
def maxSelectDigit(num_seq, select_num):
	result = [-1]
	if select_num >= len(num_seq): 
		return num_seq
	while select_num > 0:
		start = result[-1] + 1
		end = len(num_seq) - select_num + 1
		result.append(max(range(start, end), key= num_seq.__getitem__))
		select_num -= 1
	result = [num_seq[index] for index in result[1:]]
	return result


def mergeTwoSeq(seq1, seq2):
	merge_seq = []
	while seq1 or seq2:
		if seq1 >= seq2:
			merge_seq.append(seq1[0])
			seq1= seq1[1:]
		elif seq2 > seq1:
			merge_seq.append(seq2[0])
			seq2 = seq2[1:]
	return merge_seq

# Test for maxSelectDigit
# num_seq = [6,7,4,5]
# select_num = 6
# print maxSelectDigit(num_seq, select_num)


# Test for mergeTwoSeq
# seq1 = [2,3,4,2,7,1]
# seq2 = [4,1,4,5]
# print mergeTwoSeq(seq1,seq2)


def createMaximumNumber(nums1, nums2, k):
	length1 = len(nums1)
	length2 = len(nums2)
	maxAns = [0] * k
	for select_num in range(k+1):
		j = k - select_num
		if select_num > length1 or j > length2:
			continue
		seq1 = maxSelectDigit(nums1, select_num)
		seq2 = maxSelectDigit(nums2, j)
		merge_seq = mergeTwoSeq(seq1, seq2)
		maxAns = max(maxAns, merge_seq)
	return maxAns

nums1 = [8,6,9]
nums2 = [1,7,5]
k = 3
print createMaximumNumber(nums1, nums2, k)
		
