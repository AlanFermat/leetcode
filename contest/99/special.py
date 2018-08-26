from collections import Counter
def numSpecialEquivGroups(A):
	"""
	:type A: List[str]
	:rtype: int
	"""
	def isSameSpecialGroup(a,b):
		if len(a) != len(b):
			return False
		if len(a) == 1:
			return a == b
		n = len(a)
		odd1, odd2 = a[1:n:2], b[1:n:2]
		if Counter(odd1) != Counter(odd2):
			return False
		even1, even2 = a[:n:2], b[:n:2]     
		if Counter(even1) != Counter(even2):
			return False        
		return True
	
	res = 0
	while A:
		node = A.pop(0)
		idx = 0
		n = len(A)
		while n > 0 and idx < n:
			if isSameSpecialGroup(A[idx],node):
				del A[idx]
				n -= 1
			else:
				idx += 1
		res += 1
	return res


A = ["abc","acb","bac","bca","cab","cba"]
print (numSpecialEquivGroups(A))

