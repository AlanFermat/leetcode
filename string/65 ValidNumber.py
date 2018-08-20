def valid(s):
	try:
		float(s)
	except ValueError: return False
	else: return True

s = "inf"
print (valid(s))