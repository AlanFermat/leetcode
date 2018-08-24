from collections import defaultdict as dd
def areSentencesSimilar(words1, words2, pairs):
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
	for word in words1:
		g[word].add(word)
	for a,b in pairs:
		g[a].add(b)
		g[b].add(a)
	i = 0
	while i < m:
		if words1[i] in g[words2[i]]:
			i += 1
		else:
			return False
	return True

words2 = ["great"]
words1 =["great"]
pairs = []
print (areSentencesSimilar(words1, words2, pairs))
