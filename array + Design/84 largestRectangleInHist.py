class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        elif n == 1:
            return heights[0]
        else:
            maxA = max(heights)
            s = []
            i = 0
            while i < n:
                if not s:
                    s.append(i)
                    i += 1
                else:
                    if heights[i] >= heights[s[len(s)-1]]:
                        s.append(i)
                        i += 1
                    else:
                        while s and heights[i] < heights[s[len(s)-1]]:
                            tp = s.pop()
                            if not s:
                                area = heights[tp]*i
                                maxA = max(maxA, area)
                            else:
                                area = heights[tp]*(i-1-s[len(s)-1])
                                maxA = max(maxA, area)
            while s:
                tp = s.pop()
                if not s:
                    area = heights[tp]*i
                    maxA = max(maxA, area)
                else:
                    area = heights[tp]*(i-s[len(s)-1]-1)
                    maxA = max(maxA, area)
            return maxA
                                
                            
                            
                            
                            
                    
            
        