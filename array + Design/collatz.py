def solve(n):
	maxStep = 0
	for i in range(1, n+1):
		maxStep = max(collatzSolve(i), maxStep)
	return maxStep


def collatzSolve(n):
	step = 0
	while n != 1:
		step += 1
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
	return step

print (solve(6))

# 1, 0 step
# 2, 1, 1 step
# 3, 10, 5, 16, 8, 4, 2, 1, 7 step
# 4, 2, 1, 2 step
# 5, 16, 8, 4, 2, 1, 5 step
# 6, 




