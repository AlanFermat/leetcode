def score(p):
	idx = 0
	stack = []
	n = len(p)
	while idx < n:
		w = p[idx]
		if w == "(":
			stack.append(w)
		else:
			if stack[-1] == "(":
				stack.pop()
				stack.append(1)
			else:
				temp = 0
				last = stack[-1]
				while last != "(":
					temp += last
					stack.pop()
					last = stack[-1]
				temp = temp * 2
				stack.pop()
				stack.append(temp)
		idx += 1
	return sum(stack)


p = "(())((()()()))"
print (score(p))