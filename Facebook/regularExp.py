def isMatch(s, p):
	"""
	:type s: str
	:type p: str
	:rtype: bool
	"""
	# table[i][j] means the match 
	# between p[:i] and s[:j]
	# table[0][0] matching two empty strings
	# table[1][1] matching p[0] and s[0]
	m = len(s)
	n = len(p)
	table = [[False] * (m+1) for _ in range(n+1)]
	table[0][0] = True
	for i in range(2, n+1):
		table[i][0] = table[i-2][0] and p[i-1] == "*"
	# print (table)
	for i in range(1, n+1):
		for j in range(1, m+1):
			# print (table)
			if p[i-1] != "*":
				table[i][j] = table[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == ".")
			else:
				table[i][j] = table[i-2][j] or table[i-1][j]
				if p[i-2] == s[j-1] or p[i-1] == ".":
					table[i][j] = table[i][j] or table[i][j-1]
	return table[-1][-1]


p = "ab*"
s = "abb"
print (isMatch(s,p))

# table 1 1 t 
# table 1 2 F
# table 1 3 F
# table 1 4 F
# table 2 1 t



