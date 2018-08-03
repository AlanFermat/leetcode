class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        temp = {}
        for i in range(m+1):
            temp[i] = {}
            for j in range(n+1):
                temp[i][j] = False
        temp[m][n] = True
        for i in range(m,-1,-1):
            for j in range(n-1,-1,-1):
                check = i < m and p[j] in {'.',s[i]}
                if j+1 < n and p[j+1] == '*':
                    temp[i][j] = temp[i][j+2] or (check and temp[i+1][j])
                else:
                    temp[i][j] = check and temp[i+1][j+1]
        return temp[0][0]
