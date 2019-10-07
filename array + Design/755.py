def solve(heights, V, K):
	n = len(heights)
	for _ in range(V):
		mark = K
		best = K
		left = K - 1
		right = K + 1
		while left > -1 and heights[left] <= heights[mark]:
			if heights[left] < heights[mark]:
				best = left
			mark = left
			left -= 1
		if best != K:
			heights[best] += 1
			continue
		while right < n and heights[right] <= heights[mark]:
			if heights[right] < heights[mark]:
				best = right
			mark = right
			right += 1
		heights[best] += 1
	return heights



heights = [3,1,3]
V = 5
K = 1

print (solve(heights, V, K))
