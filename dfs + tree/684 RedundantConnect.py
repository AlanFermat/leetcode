from collections import defaultdict as dd
def findRedundantConnection(edges):
	"""
	:type edges: List[List[int]]
	:rtype: List[int]
	"""
	d = dd(set)
	for u, v in edges:
		d[u].add(v)
		d[v].add(u)
	v = {}
	for i in range(n):
		v[i] = False
	