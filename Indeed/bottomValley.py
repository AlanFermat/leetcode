def bottom(s):
	n = len(s)
	l = 0
	r = n - 1
	while l < r:
		mid = (l+r)//2
		if s[mid] < s[mid+1]:
			r = mid
		else:
			l = mid + 1
	return l

s = [1,3,2,5,6,7,8,9,10,11,12,14,14,15,16,17,18,19,20]
bottom(s)