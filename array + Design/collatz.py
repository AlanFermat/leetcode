def solve(n):
	step = 0
	while n != 1:
		step += 1
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
	return step

print (solve(3))




