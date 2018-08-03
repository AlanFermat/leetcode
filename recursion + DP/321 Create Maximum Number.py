class Solution(object):
    
    
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        length1 = len(nums1)
        length2 = len(nums2)
        maxAns = [0] * k
        for select_num in range(k+1):
            if select_num > length1 or k - select_num > length2:
                continue
            seq1 = self.maxSelectDigit(nums1, select_num)
            seq2 = self.maxSelectDigit(nums2, k - select_num)
            maxAns = max(self.mergeTwoSeq(seq1, seq2), maxAns)
        return maxAns
    
    def maxSelectDigit(self,num_seq, select_num):
        result = [-1]
        if select_num >= len(num_seq): 
            return num_seq 
        if select_num == 0:
            return []
        while select_num > 0:
            start = result[-1] + 1
            end = len(num_seq) - select_num + 1
            result.append(max(range(start, end), key= num_seq.__getitem__))
            select_num -= 1
        result = [num_seq[index] for index in result[1:]]
        return result
    
    def mergeTwoSeq(self,seq1, seq2):
        merge_seq = []
        while seq1 or seq2:
            if seq1 >= seq2:
                merge_seq.append(seq1[0])
                seq1 = seq1[1:]
            elif seq2 > seq1:
                merge_seq.append(seq2[0])
                seq2 = seq2[1:]
        return merge_seq

