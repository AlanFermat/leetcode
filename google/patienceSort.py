# from bisect import bisect_left

def sol(heights):
	piles = []
	def binarySearch(a, x, lo, hi):
		while lo < hi:
			mid = (lo+hi)//2
			if a[mid][0] <= x: lo = mid+1
			else: hi = mid
		return lo

	
	for num in heights:
		i = binarySearch(piles, num, 0, len(piles))
		if i != len(piles):
			piles[i].insert(0,num)
		else:
			piles.append([num])
	return piles

heights = [1,2,3,3,2]
print (sol(heights))
