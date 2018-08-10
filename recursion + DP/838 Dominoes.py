def dom(dominoes):
	if not dominoes or len(dominoes) == 1:
		return dominoes
	symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
	symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
	ans = list(dominoes)
	for (start, x), (end,y) in zip(symbols, symbols[1:]):
		print (ans)
		if x == y:
			for k in range(start+1, end):
				ans[k] = x
		elif x == "R" and y == "L":
			length = end - start + 1
			if length % 2 == 0:
				mid = start + length // 2
				for k in range(start, mid):
					ans[k] = x
				for k in range(mid, end+1):
					ans[k] = y
			else:
				mid = start + length // 2
				ans[mid] ="."
				for k in range(start, mid):
					ans[k] = x
				for k in range(mid+1, end+1):
					ans[k] = y
	return "".join(ans)





dominoes = ".R.R...LR..R.."

print (dom(dominoes))

