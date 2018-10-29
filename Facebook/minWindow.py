def minWindow(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: str
	"""
	t_map, s_map = [0]*257, [0]*257
	minLen = float("inf")
	for l in t:
		t_map[ord(l)] += 1
	n = len(s)
	i, j = 0, len(t) -1
	for k in range(i, j+1):
		s_map[ord(s[k])] += 1
	global_f = False
	while i < n and j < n:
		flag = True
		for idx in range(len(t_map)):
			if s_map[idx]<t_map[idx]:
				flag = False
				break
		if flag:
			global_f = True
			if j - i +1 < minLen:
				idx1, idx2 = i, j
				minLen = j - i +1
			s_map[ord(s[i])] -= 1
			i += 1
		else:
			j += 1
			if j < n:
				s_map[ord(s[j])] += 1
	return s[idx1:idx2+1]



s = "a"
t = "a"
print (minWindow(s, t))




