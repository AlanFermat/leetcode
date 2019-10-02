from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] # store the large number
        self.maxHeap = [] # store the small number
        self.median = None
        

    def addNum(self, num: int) -> None:
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))
        if abs(len(self.minHeap) - len(self.maxHeap)) > 0:
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0]-self.maxHeap[0]) / 2.0
        else:
            self.median = self.minHeap[0]
        

    def findMedian(self) -> float:
        return self.median

hf = MedianFinder()
hf.addNum(1)
hf.addNum(2)
hf.addNum(3)
print (hf.findMedian())

