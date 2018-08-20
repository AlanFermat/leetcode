def findAnagrams(s, p):
	"""
	:type s: str
	:type p: str
	:rtype: List[int]
	"""
	ans = []
	temp1, temp2 = [0]*26, [0]*26
	for char in p:
		temp1[ord(char) - 97] += 1
	n = len(p)
	count = 0
	print (temp1)
	for j in range(len(s)):`
		temp2[ord(s[j]) - 97] += 1
		count += 1


		if count > n:
			temp2[ord(s[j - n])-97] -= 1
		if temp2 == temp1:
			ans.append(j-n+1)
	return ans

s = "cbaebabacd"
p = "abc"

print (findAnagrams(s,p))