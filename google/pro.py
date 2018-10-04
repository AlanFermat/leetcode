def solution(S, K):
	# write your code in Python 3.6
	n = len(S)
	if K == n:
		og = S.split("-")
		return "".join(og).upper()
	else:
		og = S.split("-")
		st = list("".join(og))
		m = len(st)
		idx = m - 1
		cnt = 0
		while idx > -1:
			cnt += 1
			print (idx, cnt)
			if cnt == K:
				st.insert(idx, "-")
				cnt = 0
				idx -= 1
			else:
				idx -= 1
		if st[0] == "-":
			st.pop(0)
		return "".join(st).upper()

S = "k"
K = 1
print (solution(S, K))
