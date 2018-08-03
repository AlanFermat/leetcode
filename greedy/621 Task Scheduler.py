class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        if not tasks:
            return 0
        for i in range(len(tasks)):
            d[tasks[i]] = d.get(tasks[i],0)  + 1
        m = max(d.values())
        count = 0
        for i in d:
            if d[i] == m:
                count += 1
        return max((m-1)*(n+1) + count, sum(d.values()))
