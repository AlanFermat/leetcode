def reverse(x):
	factor = 1
	result = 0
	if x < 0:
		factor = -1
		x = abs(x)
	while x > 0:
		if result > (2**31-1 // 10):
			result = 0
			break
		else:
			result = result*10 + x%10
			x = x // 10

	return result*factor


print (reverse(-1000))