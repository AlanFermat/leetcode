def decode(s):
	"""
		Decode the given reversed ASC II string
	"""
	s = s[::-1]
	idx = 0
	n = len(s)
	asc_list = []
	while idx < n:
		if int(s[idx]) == 1:
			asc_list.append(s[idx:idx+3])
			idx += 3
		else:
			asc_list.append(s[idx:idx+2])
			idx += 2
	decoded_word = ""
	for asc_code in asc_list:
		decoded_word += chr(int(asc_code))
	print  decoded_word



	

s = "23511011501782351112179911801562340161171141148"
decode(s)