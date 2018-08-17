def valid(n, edges):
	d = {i:set() for i in range(n)}
	for x,y in edges:
		d[x].add(y)
		d[y].add(x)
	v = {}
	for i in range(n):
		v[i] = False
	start = list(d.keys())[0]
	q = [start]
	while q:
		node = q.pop(0)
		if v[node]:
			return False
		else:
			v[node] = True
			for nbr in d[node]:
				d[nbr].remove(node)
				q.append(nbr)
			del d[node]

	return not d

