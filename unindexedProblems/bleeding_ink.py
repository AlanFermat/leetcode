from heapq import *
def bleed_ink(m, n, inks):
	mat = [[0 for _ in range(n)] for _ in range(m)]
	heap = []
	for ink in inks:
		x, y, val = ink[0], ink[1], ink[2]
		heappush(heap, [-val, x, y])

	while heap:
		v, x, y = heappop(heap)
		val = -v
		if val > mat[x][y]:
			if x > -1:
				heappush(heap, [-val+1, x-1, y])
			if y > -1:
				heappush(heap, [-val+1, x, y-1])
			if x + 1 < m:
				heappush(heap, [-val+1, x+1, y])
			if y + 1 < n:
				heappush(heap, [-val+1, x, y+1])
	res = 0
	for nums in mat:
		for num in nums:
			res += num
	return res

m, n = 3, 4
inks = [[0,0,255],[1,2,255]]
print (bleed_ink(m,n,inks))
# n = input()
# for cnt in range(int(n)):
# 	rc = input().split(" ")
# 	row, col = int(rc[0]), int(rc[1])
# 	temp = []
# 	m = input()
# 	for j in range(int(m)):
# 		st = input().split(" ")
# 		temp.append([int(st[0]), int(st[1]), int(st[2])])
# 	print (bleed_ink(row, col, temp))




