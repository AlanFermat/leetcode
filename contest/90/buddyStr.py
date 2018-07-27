from collections import Counter as C
def buddyStrings(A, B):
	"""
	:type A: str
	:type B: str
	:rtype: bool
	"""
	ca = C(A)
	cb = C(B)
	if ca != cb:
		return False
	d = 0
	for i in range(len(A)):
		d += (A[i] != B[i])
	if d == 0:
		flag = 0
		for key in ca:
			if ca[key] >1:
				flag = 1
				break
		if flag:
			return True
		return False

	if d == 2:
		return True
	return False
A = "abcc"
B = "abcc"
print (buddyStrings(A,B))