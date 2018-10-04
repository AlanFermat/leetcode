def closestStore(houses, stores):
	"""
		nlogn + mlogm
	"""
	newHouse = []
	for i, h in enumerate(houses):
		newHouse.append([h,i])
	newHouse = sorted(newHouse)
	stores = sorted(list(set(stores)))
	n = len(newHouse)
	m = len(stores)
	arr = [0] * n
	idx = 0
	start = 0
	while idx < n and start < m-1:
		mid = (stores[start] + stores[start+1])/2.0
		if newHouse[idx][0] <= mid:
			arr[newHouse[idx][1]] = stores[start]
			idx += 1
		else:
			start += 1
	while idx < n:
		arr[newHouse[idx][1]] = stores[start]
		idx += 1
	return arr

	



houses = [9,5,7,9,6]
stores = [3,8,8,9,7,10]
# houses = [1,5,20,11,16]
# stores = [5,10,17]
print (closestStore(houses, stores))

