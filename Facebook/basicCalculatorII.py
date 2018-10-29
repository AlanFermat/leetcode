def cal(s):
	if not s:
		return 0
	n = len(s)
	idx = 0
	num = 0
	stack = []
	sign = "+"
	while idx < n:
		c = s[idx]
		if c.isdigit():
			num = int(c) + 10 * num 
		if (not c.isspace() and not c.isdigit()) or idx == n - 1:
			if sign == "+":
				stack.append(num)
			elif sign == "-":
				stack.append(-num)
			elif sign == "*":
				mul = stack.pop()
				stack.append(mul * num)
			else:
				div = stack.pop()
				if div < 0 and div%num != 0:
					stack.append(div//num + 1)
				else:
					stack.append(div//num)
			sign = c
			num = 0
		idx += 1
	print (sum(stack))
	return sum(stack)


test1 = "3+2*2"

cal(test1)


# print (-6%6)
