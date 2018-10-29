from heapq import *

class distance(object):
	"""docstring for distance"""
	def __init__(self, d, x, y):
		self.dist = d
		self.x = x
		self.y = y

	def __lt__(self, other):
		if self.dist == other.dist:
			return self.x > other.x
		return self.dist > other.dist

	def __eq__(self, other):
		return self.dist == other.dist and self.x == other.x and self.y == other.y
		


def function(d, k):
	dist = []
	for coord in d:
		dist.append([coord[0]**2 + coord[1] ** 2,coord[0],coord[1]])
	heap = []
	res = []
	for a, x, y in dist:
		if len(heap) <= k:
			heappush(heap, distance(a,x,y))
		else:
			heappush(heap, distance(a,x,y))
			heappop(heap)

	while len(heap) > k:
		heappop(heap)
	while heap:
		dObj = heappop(heap)
		res.append([dObj.dist, dObj.x, dObj.y])
	return res[::-1]


d = [[3,4],[4,5],[4,3],[5,6],[1,2]]
k = 2
print (function(d,k))

