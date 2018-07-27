from ListNode import *
def reorder(head):
	if not head:return None
	it = curr = head 
	# construct a reverse list
	p_head = p = ListNode(it.val)
	length = 1
	while it.next:
		it = it.next
		length += 1
		p.next = ListNode(it.val)
		p = p.next
	tail = reverse(p_head)

	# construct the reordered list
	count = 0
	while count < length:
		store = tail.next
		temp = curr.next
		curr.next = tail
		count += 1
		if count == length:
			curr.next = None
			break
		tail.next = temp
		count += 1
		if count == length:
			curr.next.next= None
			break
		curr = temp
		tail = store
		# show(head)
	return head

def reverse(head):
	prev = None
	curr = head
	while curr:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
	return prev


head = g = ListNode(6)
for _ in range(3):
	g.next = ListNode(_)
	g = g.next

show(head)
show(reorder(head))