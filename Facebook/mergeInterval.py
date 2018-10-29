# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals:
            sort_list = sorted(intervals, key = self.getKey)
            i  = 0
            n = len(sort_list)
            print sort_list
            while i < n-1:
                if sort_list[i].end >= sort_list[i+1].start:
                    sort_list[i] = Interval(sort_list[i].start, max(sort_list[i+1].end, sort_list[i].end))
                    del sort_list[i+1]
                    n -= 1
                else:
                    i += 1
            return sort_list
        else:
            return []
            
        
    def getKey(self,item):
        return [item.start, item.end]