def validTree(n, edges):
	"""
	:type n: int
	:type edges: List[List[int]]
	:rtype: bool
	"""
	if n == 1 and not edges:
		return True
	if n > 1 and not edges:
		return False
	d = {}
	for i in range(len(edges)):
		d[edges[i][0]] = d.get(edges[i][0],[]) + [edges[i][1]]
		d[edges[i][1]] = d.get(edges[i][1],[]) + [edges[i][0]]
	



n = 3
edges = [[1,0],[2,0]]
print validTree(n, edges)