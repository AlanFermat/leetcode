def sqrt(x):
	"""
		x --- integer to be sqrted
	"""
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		l,r = 0, x
		while l < r:
			mid = l + (r-l)/2
			if mid * mid == x:
				return mid
			elif mid * mid < x:
				l = mid + 1
			else:
				r = mid - 1
		if l * l < x:
			return l
		elif l * l == x:
			return l
		else:
			return l - 1

for i in range(100):
	print i,sqrt(i)

				




