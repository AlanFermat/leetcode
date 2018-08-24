def countPrime(n):
	if n < 3:
		return 0
	arr = [True] * n
	# arr[k] means if k is a prime number or not
	arr[0] = False
	arr[1] = False
	for i in range(2,int(n ** 0.5)+ 1):
		if arr[i]:
			arr[i+i:n:i] = [False] * len(arr[i+i:n:i])
	return sum(arr)



	

n = 10000
print (countPrime(n))

