def numDecodings(s):
	"""
	:type s: str
	:rtype: int
	"""
	string = s
	# If the string is empty or begins with a '0', it has no valid decoding.
	if not string or string[0] == '0':
		return 0

	k_1 = 1
	
	k_2 = 1
	for i in range(1, len(string)):
		# If we encounter a zero, there are no valid one-character decodings at this position.
		if string[i] == '0':
			k_1 = 0
		
		# If we can decode a value between 10 and 26, there's also a valid two character decoding. So,
		# the current character has k_1 + k_2 decodings, and the old k_1 becomes k_2
		if string[i - 1] == '1' or string[i-1] == '2' and 0 <= int(string[i]) <= 6:
			k_1 = k_2 + k_1
			k_2 = k_1 - k_2
		
		# There's no valid two character decoding (i.e. '40'), so the old k_1 becomes k_2.
		else:
			k_2 = k_1

	return k_1

	
s = "50"
print (numDecodings(s))

