def countSubstrings(s):
	"""
	:type s: str
	:rtype: int
	"""
	n = len(s)
	isPalindrome = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		isPalindrome[i][i] = 1
	for i in range(n-1):
		if s[i] == s[i+1]:
			isPalindrome[i][i+1] = 1
	for k in range(2,n):
		for r in range(n-k):
			c = r + k
			if isPalindrome[r+1][c-1] and (s[r] == s[c]):
				isPalindrome[r][c] = 1
	
	summ = 0
	print (isPalindrome)
	for r in range(n):
		for c in range(n):
			summ += isPalindrome[r][c]
	return summ

s = "aaaaa"
print (countSubstrings(s))
			