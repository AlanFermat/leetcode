from heapq import *

"""
	This is a min heap
"""
heap = []
heappush(heap, 1)
heappush(heap, 3)
heappush(heap, 3)
heappush(heap, -1)
print (len(heap))
print (heappop(heap))