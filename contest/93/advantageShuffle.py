from collections import defaultdict as df
def shuffle(A, B):
	"""
		O(n^2)
	"""
	n = len(A)
	new = [float('inf') for i in range(n)]
	compare_pos = df(list)
	for i in range(n):
		for j in range(n):
			if A[i] > B[j]:
				compare_pos[i] += [j]
	trash = []
	reorder= {}
	already = set([])
	def getMax(B, indices):
		max_idx = -1
		max_val = -float('inf')
		for p in indices:
			if B[p] > max_val:
				max_val = B[p]
				max_idx = p
		return max_idx
	for idx in range(n):
		if idx not in compare_pos or not compare_pos[idx]:
			trash.append(idx)
		else:
			index = getMax(B, compare_pos[idx])
			compare_pos[idx].remove(index)
			while compare_pos[idx] and index in already:
				index = getMax(B,compare_pos[idx])
				compare_pos[idx].remove(index)
			if index not in already:
				already.add(index)
				reorder[idx] = index
				continue
			if index in already:
				trash.append(idx)
	for key in reorder:
		new[reorder[key]] = A[key]
	for k in range(n):
		if new[k] == float('inf'):
			new[k] = A[trash.pop()]
	return new

A = [1,2,3,4,5]
B = [3,2,4,1,5]


def advShuffle(A, B):
	n = len(A)
	a = sorted(A)
	b = sorted([(B[i],i) for i in range(n)])
	ans = []
	trash = []
	i, j = 0,0 
	while i < n and j < n:
		if a[i] > b[j][0]:
			ans.append(a[i])
			j += 1
			i += 1
		else:
			trash.append(a[i])
			i += 1
	ans += trash
	res = [-1 for _ in range(n)]
	for ii in range(n):
		res[b[ii][1]] = ans[ii]
	return res


print (advShuffle(A, B))



	


			




