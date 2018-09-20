def findPermutation(s):
	"""
	:type s: str
	:rtype: List[int]
	"""
	if not s:
		return []
	n = len(s)
	res = list(range(1, n+2))
	start = 0
	end = 1
	while end < n + 1:
		if s[end-1] == "I":
			start = end
			end += 1
		else:
			res.insert(start, res[end])
			del res[end+1]
			end += 1
		print (res, start, end)
	return res

s = "DDIIDI"
print (findPermutation(s))