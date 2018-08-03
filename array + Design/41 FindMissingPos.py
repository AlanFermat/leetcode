class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        m = min(nums)
        M = max(nums)
        if M < 1 or m > 1:
            return 1
        temp = list(range(1,M+1))
        for i in range(len(nums)):
            if nums[i] > 0:
                temp[nums[i]-1] = -1
        idx = 0
        while idx < len(temp):
            if temp[idx] != -1:
                return temp[idx]
            idx += 1
        return M+1
        
