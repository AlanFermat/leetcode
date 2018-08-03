def findComplement(num):
	"""
        :type num: int
        :rtype: int
    """
	index = 0
	for power in range(33):
		if 2 ** power > num:
			index = power
			break
	return 2 ** index -1 -num

print findComplement(7)