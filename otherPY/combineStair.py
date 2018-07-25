def climbStairs(n):
	#note that the way to reach ith stair
	#is either from i-1 th or from i-2 th
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		way = [0] * n
		way[0] = 1
		way[1] = 2
		for i in range(2,n):
			way[i] = way[i-1] + way[i-2]
		return way[n-1]

print climbStairs(3)
