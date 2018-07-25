def generate(arr):
	ans = []
	gen = perm(arr)
	for i in gen:
		ans.append(list(i))
	return ans

def perm(arr):
	n = len(arr)
	gen = []
	if n == 0:
		return [tuple([])]
	else:
		for i in range(n):
			p = arr[i]
			arr[0],arr[i] = arr[i], arr[0]
			k = perm(arr[1:])
			s = set(k)
			gen += [tuple([p]) + x for x in s]
		gen = set(gen)
		return gen
arr = [1,1,2]
print generate(arr)


