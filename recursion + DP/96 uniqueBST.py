def uniqueBST(n):
	f = []
	for i in range(n+2):
		f.append(0)
	f[0] = 1
	f[1] = 1
	for k in xrange(2,n+1):
		for j in xrange(k):
			f[k] += f[j]*f[k-1-j]
	return f[n]

print uniqueBST(10)