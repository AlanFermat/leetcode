def solve(cityList):
	g = {}
	res = []
	indegree = {}
	for l in cityList:
		if len(l) == 1:
			g[l[0]] = set()
			indegree[l[0]] = indegree.get(l[0], 0)
		for idx in range(len(l) - 1):
			if l[idx] not in g:
				g[l[idx]] = set()
			g[l[idx]].add(l[idx + 1])
			g[l[idx + 1]] = g.get(l[idx + 1], set())
			indegree[l[idx]] = indegree.get(l[idx], 0)
			indegree[l[idx + 1]] = indegree.get(l[idx + 1], 0) + 1
	# print(indegree)
	# print(g)
	q = []
	for node in indegree:
		if indegree[node] == 0:
			q.append(node)
	while q:
		node = q.pop(0)
		res.append(node)
		for nbr in g[node]:
			degree = indegree.get(nbr) - 1
			indegree[nbr] = degree
			if degree == 0:
				q.append(nbr)
	return res


cityList = [[3, 5, 7, 9], [2, 3, 8], [5, 8], [10]]
print (solve(cityList))


