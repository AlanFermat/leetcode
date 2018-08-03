def scramble(arr1,arr2):
	m = len(arr1)
	n = len(arr2)
	if m != n:
		return False
	if arr1 == arr2:
		return True
	if sorted(arr1) != sorted(arr2):
		return False
	for i in range(1,m):
		if (scramble(arr1[:i],arr2[:i]) and scramble(arr1[i:],arr2[i:])) or \
			(scramble(arr1[:i], arr2[-i:]) and scramble(arr1[i:],arr2[:-i])):
			return True
	return False

arr1 = "abcde"
arr2 = "caebd"
print scramble(arr1, arr2)

