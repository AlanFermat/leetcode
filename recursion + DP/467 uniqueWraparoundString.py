from collections import defaultdict as dd
def wraparound(p):
	if not p:
		return 0
	possible = dd(int)
	start, end = 0, 1
	p = "9" + p
	n = len(p)
	while end < n:
		if p[end-1] + p[end] not in "abcdefghijklmnopqrstuvwxyza":
			start = end
		possible[p[end]] = max(possible[p[end]], end - start+1)
		end += 1
		print (possible)
	return sum(possible.values())

s = "zabc"
wraparound(s)

