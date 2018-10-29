def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums or len(nums) == 1:
        return 0
    n = len(nums)
    start, end, step = 0, 0, 0
    while end < n-1:
        step += 1
        maxGet = end
        for pos in range(start, end+1):
            maxGet = max(maxGet, pos + nums[pos])
        start = end
        end = maxGet
    return step

nums = [1,1,1,1,1,1,1,1,1,1,1]
print (jump(nums))