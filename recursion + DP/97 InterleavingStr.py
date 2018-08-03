class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        p = len(s3)
        if m + n != p:
            return False
        else:
            S = {}
            S[0] = {}
            S[0][0] = True
            for i in range(1,m+1):
                if s1[i-1] == s3[i-1]:
                    S[0][i] = True and S[0][i-1]
                else:
                    S[0][i] = False
            for j in range(1,n+1):
                S[j] = {}
                if s2[j-1] == s3[j-1]:
                    S[j][0] = True and S[j-1][0]
                else:
                    S[j][0] = False
            for i in range(1,n+1):
                for j in range(1,m+1):
                    S[i][j] = (s2[i-1] == s3[i+j-1] and S[i-1][j]) or (s1[j-1] == s3[i+j-1] and S[i][j-1])   
            return S[n][m]
