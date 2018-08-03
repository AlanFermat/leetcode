from graph import *
from random import *
# digraph = {'A':set(['C']),
# 			'B':set(['C','D']),
# 			'C':set(['E']),
# 			'D':set(['F']),
# 			'E':set(['F','H']),
# 			'F':set(['G']),
# 			'G':set([]),
# 			'H':set([])}
# g = Graph(digraph)

def topologicalSort(startnode,g,visit, s):
	visit[startnode] = True
	for nbr in g.nodes():
		if visit[nbr] == False:
			visit[nbr] = True
			topologicalSort(nbr,g,visit, s)
	s.insert(0, startnode)

def topoDriver(g):
	visit= {}
	stack = []
	for node in g.nodes():
		visit[node] = False
	startnode = choice(g.nodes())
	while False in visit.values():
		if visit[startnode] == False:
			topologicalSort(startnode, g, visit, stack)
	return stack

# topoDriver(g)