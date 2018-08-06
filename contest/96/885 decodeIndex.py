def decodeAtIndex(S, K):
	"""
	:type S: str
	:type K: int
	:rtype: str
	"""
	idx = 0
	curr = 0
	n = len(S)
	old = 0
	while idx < n:
		char = S[idx]
		old = curr
		if not char.isdigit():
			curr += 1
			if curr >= K:
				return S[idx]
		else:
			curr = int(char) * curr
			if curr >= K:
				return decodeAtIndex(S, (K-1)%old + 1)
		idx += 1

K = 100039


s = "y959q969u3hb22odq595"
print (decodeAtIndex(s,K))




			