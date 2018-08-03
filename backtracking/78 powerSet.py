def power(s):
	p = [[]]
	for element in s:
		p.extend([[element] + i for i in p])
	return p	


def pow(s):
	if s:
		a = s.pop()
		remaining = pow(s)
		return remaining + [[a] + i for i in remaining]
	return [[]]

def powerSet(s):
	if s:
		a = s.pop()
		for p in powerSet(s):
			yield [a] + p
			yield p 
	else:
		yield []



s = [1,2,3]
print (list(powerSet(s)))
# print pow(s)

