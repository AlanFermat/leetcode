class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        d = set(nums)
        res = 0
        for i in range(len(nums)):
            count = 0
            if nums[i]-1 not in d:
                start = nums[i]
                while start in d:
                    start += 1
                    count += 1
                res = max(res, count)
        return res                    
                
        
                
        
        
            
            
        
        
        