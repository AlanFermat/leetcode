class LRUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.mapping = {}
		self.q = []
		for i in range(capacity):
			self.mapping[-i-1] = 0
			self.q.append(-i-1)
		

	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		if key in self.q:
			self.q.remove(key)
			self.q.append(key)
		return self.mapping.get(key,-1)
		

	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: void
		"""
		if self.mapping.get(key,-1) == -1:
			k = self.q.pop(0)
			self.q.append(key)
			self.mapping.pop(k)
			self.mapping[key] = value
		else:
			self.q.remove(key)
			self.q.append(key)
			self.mapping[key] = value

cache = LRUCache( 2 )
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)    
print cache.get(1)       
print cache.get(2)     