def linearSearch(arr, num):
	for i in range(len(arr)):
		if arr[i] == num:
			return i
	return -1
		

arr = [1,2,34,5]
num = [2]
print linearSearch(arr, num)