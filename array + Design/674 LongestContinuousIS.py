def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    max_l = 1
    idx = 0
    n = len(nums)
    l = 1
    while idx < n-1:
        if nums[idx] < nums[idx+1]:
            l += 1
            print (l)
        else:
            max_l = max(max_l, l)
            l = 1
        idx += 1
    max_l = max(max_l, l)
    return max_l

nums = [1,2,3,4]
print (findLengthOfLCIS(nums))