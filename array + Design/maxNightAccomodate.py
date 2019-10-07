def solve(arr):
	if not arr:
		return 0
	n = len(arr)
	if n == 1:
		return arr[0]
	m1 = arr[0]
	m2 = max(arr[0], arr[1])
	for i in range(2, n):
		mm = max(m1 + arr[i], m2)
		m1 = m2
		m2 = mm
	return m2


arr = [2,3,5,6,4]
print (solve(arr))