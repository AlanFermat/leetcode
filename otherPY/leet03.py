from time import time 

s = "peke"




def lengthOfLongestSubstring(s):
	counts = [-1] * 256
	start = maxLen = 0
	if len(s) == 0:
		maxLen = 0
	if len(s) == 1:
		maxLen = 1
	else:
		for item in range(len(s)):
			if counts[ord(s[item])] >= start:
				start = counts[ord(s[item])] + 1
			counts[ord(s[item])] =  item
			maxLen = max(maxLen, item-start +1)
	return maxLen

def lengthOfLongestSubseq(s):
	maxLen = 0
	counts = [0] * 256
	if len(s) == 0:
		maxLen = 0
	if len(s) == 1:
		maxLen = 1
	else:
		for item in range(len(s)):
			if counts[ord(s[item])] == 0:
				counts[ord(s[item])] += 1
		maxLen = sum(counts)
	return maxLen 

t0 = time()
print (lengthOfLongestSubstring(s))

t1 = time()
print(str(t1-t0))







