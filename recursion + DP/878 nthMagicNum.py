def nthMagicalNumber(N, A, B):
	"""
	:type N: int
	:type A: int
	:type B: int
	:rtype: int
	"""
# 
	if A >= B:
		A, B = B, A
	lower, upper = A, A*N
	def gcd(x, y):
		if x == y:
			return x
		if x > y:
			x, y = y, x
		while x:
			x, y = y % x, x
		return y
	lcm_A_B = A * B // gcd(A,B)
	def getMagic(x):
		return x//A + x//B - x//lcm_A_B
	def binarySearch(l, r, goal):
		mid = (l + r)//2
		if getMagic(mid) == goal:
			if not mid % A or not mid % B:
				return mid
			else:
				return binarySearch(l,mid-1,goal)
		elif getMagic(mid) > goal:
			return binarySearch(l,mid-1,goal)
		else:
			return binarySearch(mid+1,r,goal)
	return binarySearch(lower, upper, N)% (10**9 + 7)
	# return arr[N] % (10**9 + 7)



def gcd(x, y):
	if x == y:
		return x
	if x > y:
		x, y = y, x
	while x:
		x, y = y % x, x
	return y


N = 4
A = 2
B = 5

print (nthMagicalNumber(N,A,B))

