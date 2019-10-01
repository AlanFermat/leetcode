def findAllAnagram(s, p):
	ans = []
	d = dict() 
	for letter in p:
		d[letter] = d.get(letter, 0) + 1
	cad = dict()
	idx = len(p) - 1
	wcad = s[:idx+1]
	for i in range(idx+1):
		cad[s[i]] = cad.get(s[i], 0) + 1
	if check(d, cad):
		ans.append(0)
	j = idx + 1
	while j < len(s):
		cad[s[j-len(p)]] = cad[s[j-len(p)]] - 1
		cad[s[j]] = cad.get(s[j], 0) + 1
		if check(d, cad):
			ans.append(j-idx)
		j += 1
	return ans


def check(d, cad):
	for k in d:
		if cad.get(k, 0) != d.get(k, 0):
			return False
	return True

s = "cbaebabacd"
p = "abe"

print (findAllAnagram(s, p))
