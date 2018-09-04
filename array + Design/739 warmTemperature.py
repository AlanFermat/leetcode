def warm(temperatures):
	if not temperatures:
		return []
	stack = []
	n = len(temperatures)
	res = [0 for _ in range(n)]
	for i, t in enumerate(temperatures):
		while stack and stack[-1][0] < t:
			val, pos = stack.pop()
			res[pos] = i - pos 
		stack.append((t,i))
				
	return res