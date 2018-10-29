from collections import defaultdict as dd
def alienOrder(arr): 
	g = dd(set)
	allLetter = set()
	for word in arr:
		print (word)
		for l in word:
			allLetter.add(l)
		if len(word) == 1:
			g[word[0]] = set([])
			continue
		for i in range(len(word)-1):
			if word[i] != word[i+1]:
				g[word[i]].add(word[i+1])

	print (g)
	return topologicalSort(g, allLetter)


def topologicalSort(g, allLetter):
	v = {}
	for l in allLetter:
		v[l] = 0
	stack = []
	for i in g.keys():
		if not v[i]:
			if not dfs(i, v, g, stack):
				return [""]
	return stack

def dfs(node, v, g, stack):
	if v[node] == -1:
		return False
	if v[node] == 1:
		return True
	v[node] = -1
	if node in g:
		for nbr in g[node]:
			if v[nbr] != 1:
				if not dfs(nbr, v, g, stack):
					return False
	stack.insert(0, node)
	v[node] = 1
	return True
	



arr = ["eeeeerrrrrrttttyyyyyeee","weee"]
print (alienOrder(arr))

