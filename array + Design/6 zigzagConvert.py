def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        l = []
        r = numRows
        if r == 1:
            return s
        elif r == 2:
            for i in range(n):
                if i % 2 == 0:
                    l.append(s[i])
            for j in range(n):
                if j % 2 == 1:
                    l.append(s[j])
        else:
            roundOne = 2*r - 2
            for i in range(n):
                if (i+1)%roundOne == 1:
                    l.append(s[i])
            for remain in range(2,r):
                idx = roundOne + 2 - remain
                k = 0
                while k*roundOne+remain < n+1  and k*roundOne+idx < n+1:
                    l.append(s[k*roundOne+remain-1])
                    l.append(s[k*roundOne+idx-1])
                    k += 1
                if k * roundOne+remain < n+1:
                    l.append(s[k*roundOne+remain-1])
            for i in range(n):
                if (i+1)%roundOne == r:
                    l.append(s[i])
        return "".join(l)
s = "l"
numRows = 2
print convert(s,numRows)
