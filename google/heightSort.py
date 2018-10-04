from heapq import *
def sol(heights):
	heap = []
	for h in heights:
		if not heap:
			heappush(heap, h)
		else:
			l = []
			while heap:
				minimum = heappop(heap)
				if minimum > h:
					heappush(heap, h)
					break
				else:
					l.append(minimum)
			if not heap:
				heappush(heap, h)
			while l:
				heappush(heap, l.pop())
		print (heap)
	return len(heap)


heights = [3,3,3,3,34,4,4,5]
print (sol(heights))
