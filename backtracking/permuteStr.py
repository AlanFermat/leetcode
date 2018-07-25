def toString(s):
	return ''.join(s)

def permute(s,l,r):
	if l == r:
		print toString(s)
	else:
		for i in range(l,r+1):
			s[i], s[l] = s[l], s[i]
			permute(s,l+1,r)
			s[l], s[i] = s[i],s[l]

s = ['a','b','c']
l = 0
r = 2
permute(s,l,r) 

