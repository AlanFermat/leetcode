def reconstruct(arr):
	if not arr:
		return []
	arr = sorted(arr, key = lambda x: [-x[0], x[1]])
	print arr
	temp = []
	for p in arr:
		temp.insert(p[1],p)
	print temp

arr=  [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
reconstruct(arr)
