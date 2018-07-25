def decode(s):
	n = len(s)
	idx= 0
	stack = []
	stack.append(["",1])
	num = ""
	while idx < n:
		if s[idx].isdigit():
			num += s[idx]
		elif s[idx] == '[':
			stack.append(["",int(num)])
			num = ""
		elif s[idx] == ']':
			part, k = stack.pop()
			stack[-1][0] += part * k
		else:
			stack[-1][0] += s[idx]
		idx += 1
	return stack[-1][0]

s =  "2[a]12[abs4[r]]"
print decode(s)