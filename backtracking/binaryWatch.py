def binaryWatch(n):
	"""
		Return all possible times it can represent
		A binary watch has 4 LEDs on the top which represent the hours (0-11), 
		and the 6 LEDs on the bottom represent the minutes (0-59).
	"""
	return ['%d:%02d' % (h,m) for h in range(12) for m in range(60)
		if (bin(h) + bin(m)).count('1') == n]





print binaryWatch(1)

print "Hi %04s I have %04d pizzas" % ("all",44)

g = "abc1"
print [i.upper() for i in g if i.isalpha()]



# Note that %04s means we will fill the string so that the 
# length of it will become 4 (fill by blank space)
# Note that %04d means that we will fill the double so that 
# the length will be of 4 (fill by 0's)


