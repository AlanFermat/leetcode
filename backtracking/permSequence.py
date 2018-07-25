def getPermutation(n, k):
	"""
	:type n: int
	:type k: int
	:rtype: str
	"""
	l = list(range(1,n+1))
	perm = permutation(l)
	perm = sorted(perm)
	out = ""
	for i in range(len(perm[0])):
		out += str(perm[k-1][i])
	return out
def permutation(l):
	if l:
		return [p[:i]+[l[0]]+p[i:]
		   for p in permutation(l[1:])
		   for i in range(len(l))]
	return [[]]

n = 3
k = 3

print getPermutation(n,k)