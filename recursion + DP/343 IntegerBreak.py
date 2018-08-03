def integerBreak(n):
	if n == 2:
		return 1
	if n == 3:
		return 2
	if n == 4:
		return 4
	# note that we will not include 1 in 
	# our product due to optimization
	three = 0
	num = n
	while num > 6:
		num -= 3
		three += 1
	if num == 6:
		three += 2
		return 3 ** three
	if num == 5:
		three += 1
		return 3 ** three * 2 
	if num == 4:
		return 3 ** three * 4


n = 6
print (integerBreak(n))


