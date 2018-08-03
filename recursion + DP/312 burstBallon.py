class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        # P(N) O(N^3)
        B = [1] + nums + [1]
        m = len(B)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for diff in range(2, m):
            for left in range(0,m-diff):
                right = left + diff
                for k in range(left+1, right):
                    dp[left][right] = max(dp[left][right], B[left] * B[k] * B[right] + dp[left][k] + dp[k][right])
        return dp[0][m-1]