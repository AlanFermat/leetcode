def lazy_range(n):
	i = 0
	while i < n:
		yield i 
		i += 1
print lazy_range(10)

