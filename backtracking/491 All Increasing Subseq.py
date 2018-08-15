def findSubsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []
    res = set([])
    n = len(nums)
    if n == 1:
        return []
    def backtracking(res, cur,arr):
        for j in range(len(arr)):
            if arr[j] >= cur[-1]:
                cur += (arr[j],)
                res.add(cur)
                backtracking(res,cur,arr[j+1:])
                cur = cur[:-1]    
    for i in range(n-1):
        backtracking(res, (nums[i],), nums[i+1:])
    return map(list, list(res))