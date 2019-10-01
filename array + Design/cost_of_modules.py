
def cost_of_module(input):
	g, nodes_cost = init_graph(input)
	# print(g, nodes_cost)
	inv_g = {}
	for node in nodes_cost:
		inv_g[node] = []
	inv_g = inverse_graph(g, inv_g)
	# print(inv_g)
	for node in nodes_cost:
		v = init_visit(nodes_cost)
		dfs(inv_g, node, v, nodes_cost)
	print (nodes_cost)

def init_visit(nodes_cost):
	v = {}
	for node in nodes_cost:
		v[node] = False
	return v


def init_graph(input):
	g = {}
	nodes_cost = {}
	for nodes in input:
		nodes_list = nodes.split(",")
		parent = nodes_list[0]
		if nodes_cost.get(parent) is None:
			nodes_cost[parent] = 1
		if g.get(parent) is None:
			g[parent] = []
		for child in nodes_list[1:]:
			g[parent].append(child)
			if nodes_cost.get(child) is None:
				nodes_cost[child] = 1
	return g, nodes_cost

def inverse_graph(g, inv_g):
	for parent in g:
		for child in g[parent]:
			inv_g[child].append(parent)
	return inv_g


def dfs(g, node, v, nodes_cost):
	v[node] = True
	q = [node]
	while q:
		s = q.pop()
		for nbr in g[s]:
			if not v[nbr]:
				nodes_cost[node] += 1
				q.append(nbr)
				v[nbr] = True

	
	
# input2 = ["G,E","E,F,N","F,N","N"]
input = ["A,E,N,S", "S,H,N","E,N","H","N"]
cost_of_module(input)









