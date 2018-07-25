class Solution(object):
	def minEatingSpeed(self, piles, H):
		"""
		:type piles: List[int]
		:type H: int
		:rtype: int
		"""
		lo = 1
		hi = max(piles)
		num = self.getRate(piles, H, lo, hi)
		return num
	
	def getRate(self, piles, H, lo, hi):
		if lo < hi:
			mid = (lo + hi)/2
			count = self.steps(piles, mid)
			if count > H:
				return self.getRate(piles, H, mid+1, hi)
			if count <= H:
				return self.getRate(piles, H, lo, mid-1)
		else:
			return lo

		
	def steps(self, piles, a):
		c = 0
		for i in range(len(piles)):
			if piles[i] % a == 0:
				c += piles[i]/a
			else:
				c += piles[i]/a + 1
		return c


p = Solution()
piles = [3,6,7,11]

H = 8
print p.minEatingSpeed(piles,H)
