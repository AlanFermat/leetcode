from ListNode import *
def rotateRight(head, k):
	"""
	:type head: ListNode
	:type k: int
	:rtype: ListNode
	"""
	it = curr = head
	n = 0
	while it:
		n += 1
		it = it.next
	r = k % n
	# keep the order of the first n-r elements
	for _ in range(n-r-1):
		curr =  curr.next     
	temp  = curr.next
	# shift the last r elements
	curr.next = None
	start = temp
	while temp and temp.next:
		temp = temp.next
	if temp:
		temp.next = head
		return start
	return head

first = head = ListNode(1)
for _ in range(8):
	head.next = ListNode(_)
	head = head.next
show(first)
show(rotateRight(first, 27))



