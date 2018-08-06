class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0  
        dp = [0 for _ in range(n)]
        idx = 0
        while idx < n - 2:
            dif1 = A[idx+1] - A[idx]
            dif2 = A[idx+2] - A[idx+1]
            if dif1 != dif2:
                idx += 1
                continue
            dp[idx] += 1
            j = idx + 2
            while j < n-1:
                if A[j+1] - A[j] == dif1:
                    dp[idx] += 1
                    j += 1
                else:
                    break
            idx += 1
        return sum(dp)
                