class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s), len(p)
        temp = []
        for i in range(m+1):
            store = []
            for j in range(n+1):
                store.append(False)
            temp.append(store)
        temp[0][0] = True
        idx = 0
        while idx < n and p[idx]=='*':
            temp[0][idx+1] = True
            idx += 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    temp[i][j] = temp[i-1][j] or temp[i][j-1]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    temp[i][j] = temp[i-1][j-1]
        return temp[m][n]