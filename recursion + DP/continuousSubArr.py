class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        if k == 0:
            for i in range(n):
                if nums[i] != 0:
                    return False
            return True
        summation = 0
        s = {0:-1}
        for i in range(n):
            summation += nums[i]
            rem = summation % k
            if rem in s:
                if i - s[rem] >= 2:
                    return True
            else:
                s[rem] = i
        return False
        
        