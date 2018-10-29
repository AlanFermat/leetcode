def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    idx = 0
    count = 0
    n = len(nums)
    summation= 0
    sum_slot = {0:1}
    while idx < n:
        summation += nums[idx]
        count += sum_slot.get(summation-k, 0)
        sum_slot[summation] = sum_slot.get(summation, 0) + 1 
        idx += 1
    return count