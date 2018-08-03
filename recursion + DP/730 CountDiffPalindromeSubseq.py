def countPalindromicSubsequences(S):
	"""
	:type S: str
	:rtype: int
	"""
	n = len(S)
	if n == 1:
		return 1
	dp = [[0 for _ in range(n)] for _ in range(n)]



		