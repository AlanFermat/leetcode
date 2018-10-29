def nextPermuation(arr):
	n = len(arr)
	i = n - 2
	while i >= 0 and arr[i] >= arr[i+1]:
		i -= 1
	if i < 0:
		return -1
	if i >= 0:
		j = n - 1
		while j >= 0 and arr[j] <= arr[i]:
			j -= 1
		arr[i], arr[j] = arr[j], arr[i]
	p = arr[i+1:]
	arr[i+1:] = p[::-1]
	return arr


# arr = [1,2,43,8]
# print (nextPermuation(arr))

# g = 123
# print (list(str(g)))
# print ("0" < "9")



def nextGreaterElement(n):
    """
    :type n: int
    :rtype: int
    """
    l = list(str(n))
    length = len(l)
    i = length - 2
    while i >= 0 and l[i] >= l[i+1]:
        i -= 1
    if i < 0:
        return -1
    if i >= 0:
        j = length - 1
        while j >= 0 and l[j] <= l[i]:
            j -= 1
        l[i], l[j] = l[j], l[i]
    remain = l[i+1:]
    l[i+1:] = remain[::-1]
    num_str = "".join(l)
    return int(num_str)


n = 1999999
print (nextGreaterElement(n))