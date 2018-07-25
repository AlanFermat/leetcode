def validParenthensis(s):
	t = []
	n = len(s)
	longest = 0
	for i in xrange(n):
		if s[i] == '(':
			t.append(i)
		else:
			if t:
				if s[t[len(t)-1]] == '(':
					t.pop()
				else:
					t.append(i)
			else:
				t.append(i)
	if not t:
		return n
	print t
	longest = t[0] - 0
	end = n-1
	start = 0
	while t:
		start = t.pop()
		if start > 0 and end < n-1:
			longest = max(longest, end - start - 1) 
		else:
			longest = max(longest, end - start)
		end = start
	longest = longest / 2
	longest = longest * 2
	return longest



s = '())'
print validParenthensis(s)