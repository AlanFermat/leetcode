from heapq import *

h = [[1,2],[1,3],[0,4]]
g = ["a","b","c","ab"]
heapify(h)

print (heappop(h))
print (heappop(h))

heapify(g)
print (heappop(g))
print (heappop(g))