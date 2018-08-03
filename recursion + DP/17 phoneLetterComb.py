def convert(s):
	if s == '0':
		return ['0']
	if s == '1':
		return ['1']
	if s == '2':
		return ['a','b','c']
	if s == '3':
		return ['d','e','f']
	if s == '4':
		return ['g','h','i']
	if s == '5':
		return ['j','k','l']
	if s == '6':
		return ['m','n','o']
	if s == '7':
		return ['p','q','r','s']
	if s == '8':
		return ['t','u','v']
	if s == '9':
		return ['w','x','y','z']

def change(d):
	if d:
		a = d.pop()
		c = convert(a)
		return [i+j for i in c for j in change(d)]
	return []

	

def letterCombinations(digits):
	d = []
	if digits:
		for i in range(len(digits)):
			d.append(digits[i])
		p = change(d)
	return p 


s = "23"

print letterCombinations(s)