from collections import defaultdict as dd
from graphviz import Graph
from heapq import *
# def reachableNodes(edges, M, N):
# 	# this algorithm is correct but will
# 	# result in time limit exceeding on LeetCode
# 	g = dd(list)
# 	for item in edges:
# 		if item[2]:
# 			g[item[0]] += [N]
# 			g[N]+= [item[0]]
# 			num = 1
# 			while num < item[2]:
# 				N += 1
# 				g[N-1] += [N]
# 				g[N] += [N-1]
# 				num += 1
# 			g[N] += [item[1]]
# 			g[item[1]] += [N]
# 			N += 1
# 		else:
# 			g[item[0]] += [item[1]]
# 			g[item[1]] += [item[0]]
# 	visit = {}
# 	for key in g:
# 		visit[key] = False
# 	def dfs(startnode, step):
# 		if step < 0:
# 			return 
# 		visit[startnode] = True
# 		for nbr in g[startnode]:
# 			if nbr == 1:
# 				print ("reach 1")
# 				print (visit[1], step)
# 			dfs(nbr, step - 1)
# 	dfs(0, M)
# 	cnt = 0
# 	for node in visit:
# 		if visit[node]:
# 			cnt += 1
# 	return cnt, visit,g 

def reachable(edges, M, N):
	# this algorithm is based on 
	# Dijkstra 
	g = dd(dict)
	for u, v, w in edges:
		g[u][v] = w
		g[v][u] = w
	dist = {0:0}
	# pq is in the order (distance to the node from 0, that node)
	pq = [(0,0)]
	partial = {}
	ans = 0
	while pq:
		d, node = heappop(pq)
		if d > dist[node]:
			continue
		ans += 1
		for nbr, weight in g[node].items():
			further = min(weight, M-d)
			partial[(node, nbr)] = max(further,0)
			d2 = d + weight + 1
			if d2 < dist.get(nbr, M+1):
				heappush(pq,(d2,nbr))
				dist[nbr] = d2
	for u, v, w in edges:
		ans += min(w, partial.get((u,v), 0)+partial.get((v,u), 0))

	return ans









edges = [[0,1,10],[0,2,1],[1,2,2]]
M = 6
N = 3
print (reachable(edges, M, N))












			


