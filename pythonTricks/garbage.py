import gc

def make():
	l = []
	l.append(l)
	return l

print (len(make()))

