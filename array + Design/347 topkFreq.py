from collections import defaultdict as dd
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    nums = sorted(nums)
    d = dd(list)
    n = len(nums)
    idx = 0
    freq =  1
    while idx < n-1:
        if nums[idx] == nums[idx+1]:
            freq += 1
            idx += 1
        else:
            d[freq] += [nums[idx]]
            idx += 1
            freq = 1
    d[freq] += [nums[idx]]
    res = []
    fr = sorted(d.keys())
    print (d)
    while k:
        key = fr.pop()
        while d[key] and k:
            res += [d[key].pop()]
            k -= 1
    return res
nums = [1,1,1,2,2,3,4]
k = 2
topKFrequent(nums,k)