class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


def show(node):
	temp = []
	while node:
		temp.append(str(node.val))
		node = node.next
	print ("->".join(temp))