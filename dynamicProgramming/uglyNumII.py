from heapq import *
def nthUglyNumber(n):
	"""
	:type n: int
	:rtype: int
	""" 
	if n == 1:
		return 1
	ans = [1]
	have = set([1])
	heapify(ans)
	count = 1
	while count < n:
		val = heappop(ans)
		if val * 2 not in have:
			have.add(val*2)
			heappush(ans,  val * 2)
		if val * 3 not in have:
			have.add(val*3)
			heappush(ans,  val * 3)
		if val * 5 not in have:
			have.add(val*5)
			heappush(ans,  val * 5)
		count += 1
	return heappop(ans)
n = 10
print (nthUglyNumber(n))