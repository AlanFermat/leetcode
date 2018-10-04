def myPow(x, n):
	ref = str(bin(n)).replace('0b', '')[::-1]
	res, pivot = 1, x
	for r in ref:
		if (r == '1'):
			res = res * pivot
		pivot = pivot * pivot
	res = res if (n>=0) else 1 /res
	return res

print (myPow(4, 5))