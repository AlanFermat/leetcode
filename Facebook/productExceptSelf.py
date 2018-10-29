def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    p1, p2 = 1, 1
    res = [1] * n
    for i in range(n):
        res[i] *= p1
        p1 *= nums[i]
    for j in range(n-1, -1, -1):
        res[j] *= p2
        p2 *= nums[j]
    return res