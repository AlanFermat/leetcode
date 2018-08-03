def combine(digits):
	interpret = {'0':'','1':'','2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
	if len(digits) == 0:
		return []
	elif len(digits) == 1:
		return list(interpret[digits[0]])
	else:
		p = []
		addition = combine(digits[:-1])
		last = interpret[digits[-1]]
		for i in addition:
			for j in last:
				p.append(i+j)
		return p


digits = "223"
print len(combine(digits))

