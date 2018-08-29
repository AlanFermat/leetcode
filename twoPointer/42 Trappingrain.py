class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1 or len(height) == 2:
            return 0
        n = len(height)
        res = 0
        left_max, right_max = [height[0] for _ in range(n)], [height[n-1]  for _ in range(n)]
        prev = height[0]
        post = height[n-1]
        for i in range(n):
            if prev < height[i]:
                prev = height[i]
            left_max[i] = prev
        for j in range(n-1, -1, -1):
            if post < height[j]:
                post = height[j]
            right_max[j] = post
        for k in range(n):
            res += min(left_max[k], right_max[k]) - height[k]
        return res
            
        