def lengthOfLongestSubstringTwoDistinct(s):
	"""
	:type s: str
	:rtype: int
	"""
	temp = [[[],0]]
	idx = 0
	n = len(s)
	if n < 3:
		return len(s)
	while idx < n:
		if s[idx] in temp[idx][0]:
			temp.append([temp[idx][0], temp[idx][1]+1])
		else:
			if len(temp[idx][0]) < 2:
				temp.append([temp[idx][0]+[s[idx]], temp[idx][1]+1])
			if len(temp[idx][0]) == 2:
				pointer = getFirstIdxPrevChar(idx,s)
				temp.append([[s[idx-1],s[idx]],idx - pointer + 1])
		idx += 1
	print temp
	max_len = 2
	for i in range(1,len(temp)):
		if temp[i][1] <= temp[i-1][1]:
			l = temp[i-1][1]
			max_len = max(max_len,l)
		else:
			l = temp[i][1]
			max_len = max(max_len,l)
	return max_len

def getFirstIdxPrevChar(idx,s):
	temp = s[idx-1]
	while idx > 0:
		if s[idx-1] == temp:
			pointer = idx -1 
			idx -=1
		else:
			break
	return pointer


s = "ccaabbbciiccii"
print lengthOfLongestSubstringTwoDistinct(s)

