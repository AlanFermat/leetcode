def licenseKeyFormatting(S, K):
	"""
	:type S: str
	:type K: int
	:rtype: str
	"""
	string = S.split('-')
	string = "".join(string)
	string = string.upper()
	s = list(string)
	ans = []
	print s
	while s:
		temp = ""
		for i in range(K):
			if s:
				temp = s.pop() + temp
			else:
				break
		ans.insert(0,temp)
	return "-".join(ans)

S = "2231231sdssdd-5g-3-J"
K = 2
print licenseKeyFormatting(S, K)