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

def build(l):
	d = node = ListNode(0)
	while l:
		node.next = ListNode(l.pop(0))
		node = node.next
	return d.next