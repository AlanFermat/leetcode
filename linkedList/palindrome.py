from ListNode import *

def show(node):
	temp = []
	while node:
		temp.append(str(node.val))
		node = node.next
	print ("->".join(temp))

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next= ListNode(3)


def isPalindrome(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	if not head:
		return True
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	stack = []
	stack.append(slow.val)
	slow = slow.next
	while slow:
		stack.append(slow.val)
		slow = slow.next

	while stack:
		k = stack.pop()
		if k != head.val:
			return False
		head = head.next
	return True

print (isPalindrome(l1))


