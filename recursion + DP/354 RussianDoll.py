def russianDoll(envelopes):
	# # O(n^2)
	# if not envelopes:
	# 	return 0
	# n = len(envelopes)
	# envelopes = sorted(envelopes)
	# dp = [0 for _ in range(n)] # dp[i] records
	# # the LIS up to ith entry
	# dp[0] = 1
	# ans = 0
	# for i in range(n):
	# 	# up_to_j records the LIS with jth entry as its ending
	# 	up_to_j = 0
	# 	for j in range(i):
	# 		if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
	# 			up_to_j = max(up_to_j, dp[j])
	# 	dp[i] = up_to_j + 1
	# 	ans = max(dp[i], ans)
	# return ans
	# # O(N log N)
	if not envelopes:
		return 0
	envelopes = sorted(envelopes, key=lambda x:(x[0],-x[1]))
	n = len(envelopes)
	M = [None] * n
	# p = [None] * n
	L = 1
	M[0] = 0
	for i in range(1,n):
		upper, lower = L, 0
		if envelopes[M[upper-1]][1] < envelopes[i][1]:
			j = upper
		else:
			while upper > lower + 1:
				mid = (upper + lower) //2
				if envelopes[M[mid-1]][1] >= envelopes[i][1]:
					upper = mid
				else:
					lower = mid
			j = lower
		# P[i] = M[j-1]
		if j == L or envelopes[i][1] < envelopes[M[j]][1]:
			M[j] = i
			L = max(L, j+1)
		# result = []
		# pos = M[L-1]
		# for _ in range(L):
		# 	result.append(envelopes[pos])
		# 	pos = P[pos]
	return L




envelopes = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
print (russianDoll(envelopes))	


