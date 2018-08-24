from collections import defaultdict as dd
def areSentencesSimilarTwo(words1, words2, pairs):
	"""
	:type words1: List[str]
	:type words2: List[str]
	:type pairs: List[List[str]]
	:rtype: bool
	"""
	if not words1:
		return not words2
	if not words2:
		return False
	m, n = len(words1), len(words2)
	if m != n:
		return False
	g = dd(set)
	for w in words1:
		g[w].add(w)
	for a,b in pairs:
		g[a].add(b)
		g[b].add(a)
	print (g)
	idx = 0
	v = {}
	for key in g:
		v[key] = False
	def dfs(end,g, q, v):
		if not q:
			return False
		node = q.pop()
		v[node] = True
		if node == end:
			return True
		for nbr in g[node]:
			if not v[nbr]:
				q.append(nbr)
		return dfs(end, g, q, v)

	while idx < m:
		if dfs(words2[idx], g, [words1[idx]], v):
			idx += 1
		else:
			return False
	return True


words1 = ["a","very","delicious","meal"]
words2 = ["one","really","delicious","dinner"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
print (areSentencesSimilarTwo(words1, words2, pairs))


