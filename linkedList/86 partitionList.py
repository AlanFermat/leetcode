from ListNode import *
def partition(head, x):
	"""
	:type head: ListNode
	:type x: int
	:rtype: ListNode
	"""
	if not head:
		return head
	dummy = ListNode(0)
	dummy.next = head
	curr = last = mark = dummy
	while curr.next:
		if curr.next.val >= x:
			last = curr
			mark = curr.next
			break
		curr = curr.next
	stack = []
	while mark.next:
		if mark.next.val < x:
			stack.append(mark.next.val)
			mark.next = mark.next.next
		else:
			mark = mark.next
	while stack:
		val = stack.pop(0)
		temp = last.next
		last.next = ListNode(val)
		last.next.next = temp
		last = last.next
	return dummy.next

l = [3,1,2,4,1,0,6]
head = build(l)
d = partition(head,2)
show(d)









