from collections import Counter

def index(s, t):
	k = len(t)
	n = len(s)
	if k > n:
		return []
	elif k == n:
		if Counter(s) == Counter(t):
			return [0]
	else:
		ans = []
		idx = k
		t_map, s_map = [0]*256, [0]*256
		for tl in t:
			t_map[ord(tl)] += 1
		for i in range(k):
			s_map[ord(s[i])] += 1
		if s_map == t_map:
			ans += [0]
		while idx < n:
			s_map[ord(s[idx-k])] -= 1
			s_map[ord(s[idx])] += 1
			if s_map == t_map:
				ans += [idx - k +1]
			idx += 1
	return ans

s = "aaanaaa"
t = "anaa"
print (index(s,t))

