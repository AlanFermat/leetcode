from heapq import *
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        summ = float("inf")
        cost = self.getCostRate(quality, wage)
        h = []
        qsum = 0
        for i in range(len(cost)):
            r,q = cost[i]
            heappush(h, -q)
            qsum += q
            
            # get rid of the largest quality
            if len(h) > K:
                qsum += heappop(h)
                
            if len(h) == K:
                summ = min(summ, qsum * r)
                
        return summ
                
            
        
        
    
    def getCostRate(self, quality, wage):
        cost = [0 for _ in range(len(quality))]
        for i in range(len(quality)):
            cost[i] = (float ( 1.0 * wage[i] / quality[i]), quality[i])
        cost = sorted(cost, key = lambda x: x[0])
        return cost

            
        