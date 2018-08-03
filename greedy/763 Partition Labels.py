class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        maxidx = 0
        n = len(S)
        res= [[]]
        output = []
        for i in range(n):
            if i > maxidx:
                res.append([S[i]])
                maxidx = S.rfind(S[i])
            else:
                res[-1].append(S[i])
                maxidx = max(S.rfind(S[i]), maxidx)
        for j in range(len(res)):
            output.append(len(res[j]))
        return output
