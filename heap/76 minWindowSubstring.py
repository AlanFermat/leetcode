class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        temp1, temp2 = [0]*128, [0]*128
        for char in t:
            temp1[ord(char)] += 1
        m, n = len(t), len(s)
        begin, end = 0, 0 
        minWindow = n + 1
        res = ""
        while end < n:
            if end - begin + 1 < m:
                temp2[ord(s[end])] += 1
                end += 1
            else:
                temp2[ord(s[end])] += 1
                while self.hasAllIn(temp1, temp2) and end - begin + 1>= m:
                    if minWindow > end - begin + 1:
                        minWindow = end - begin + 1
                        res = s[begin:end+1]
                    temp2[ord(s[begin])] -= 1
                    begin += 1
                
                end += 1
        return res
                    

                
                
        
        
    def hasAllIn(self, temp1, temp2):
        for i in range(len(temp1)):
            if temp1[i] > temp2[i]:
                return False
        return True
                
        