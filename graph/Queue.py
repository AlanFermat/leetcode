class Queue:
	#first in first out
	"""docstring for Queue"""
	def __init__(self):
		self.items = []
		# print type(self.items)


	def __len__(self):
		return len(self.items)

	def __str__(self):
		s = ''
		for i in self.items:
			s += str(i)
		return s

	def push(self, item):
		return self.items.insert(0, item)

	def pop(self):
		return self.items.pop()

	def clear(self):
		del self.items[:]




