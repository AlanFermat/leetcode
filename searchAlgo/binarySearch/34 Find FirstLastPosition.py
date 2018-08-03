class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.find(nums,target,0 ,len(nums)-1, 0)
        n = len(nums)
        if idx > -1:
            l, r = idx, idx
            while l > -1:
                if nums[l] == target:
                    l -= 1
                else:
                    break
            while r < n:
                if nums[r] == target:
                    r += 1
                else:
                    break
            return [l+1, r-1]
        else:
            return [-1, -1]
            
    def find(self, nums, target, start, end, before):
        if start > end:
            return -1
        else:
            mid = before + (end - start) / 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return self.find(nums, target, mid+1, end, mid+1)
            else:
                return self.find(nums, target, start, mid-1, start)
            
            
            
