class Stack:
	"""docstring for Stack
	Last in First Out
	"""
	def __init__(self):
		self.items = []
	def __len__(self):
		return len(self.items)

	def __str__(self):
		s = ''
		for i in self.items:
			s += str(i)
		return s

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def clear(self):
		self.items = []
		return self.items


# container = Stack()
# container.push(2)
# container.push(4)
# container.push(5)
# print container.pop()
# print container.pop()
# print container.pop()
