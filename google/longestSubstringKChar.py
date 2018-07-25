def lengthOfLongestSubstringKDistinct(s, k):
	"""
	:type s: str
	:type k: int
	:rtype: int
	"""
	n = len(s)
	if n <= k:
		return len(s)
	temp = [[[], 0, 0]]
	idx = 0
	while idx < n:
		if s[idx] in temp[idx][0]:
			temp.append([temp[idx][0], temp[idx][1] + 1, temp[idx][2]])
		else:
			if len(temp[idx][0]) < k:
				temp.append([temp[idx][0] + [s[idx]], temp[idx][1] + 1]) 
			elif len(temp[idx][0]) == k:
				char = temp[idx][0][0]
				p = findFirstIdx(char, s, idx)
				temp.append([temp[idx][0][1:] + [s[idx]], idx - p])
		idx += 1
	maxLen = k
	for i in range(1,len(temp)):
		l = temp[i][1]
		maxLen = max(maxLen, l)
	print (temp)
	return maxLen
	
def findFirstIdx(char, s, idx):
	print (char)
	print ("idx" + str(idx))
	end = idx - 1
	pointer = 0
	while end > 0:
		if char == s[end]:
			pointer = end
			break
		else:
			end -= 1
	print ("pointer" + str(pointer))
	return pointer


s = "abaccc"
print (lengthOfLongestSubstringKDistinct(s,2))


				