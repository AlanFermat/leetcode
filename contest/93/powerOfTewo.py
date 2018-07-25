from collections import Counter as C
def reorderedPowerOf2(N):
	"""
	:type N: int
	:rtype: bool
	"""
	num_str = str(N)
	for idx in range(30):
		a = str(2 ** idx)
		if C(a) == C(num_str):
			return True
	return False

print (reorderedPowerOf2(1024 * 1024))	


