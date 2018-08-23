from collections import defaultdict as dd
def killProcess(pid, ppid, kill):
	"""
	:type pid: List[int]
	:type ppid: List[int]
	:type kill: int
	:rtype: List[int]
	"""
	if not pid:
		return []
	g = dd(set)
	for idx in range(len(ppid)):
		if ppid[idx]:
			g[ppid[ijkdx]].add(pid[idx])
	print (g)
	q = [kill]
	res = [kill]
	while q:
		node = q.pop(0)
		for nbr in g[node]:
			q.append(nbr)
			res.append(nbr)
	return res

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
print (killProcess(pid,ppid,kill))