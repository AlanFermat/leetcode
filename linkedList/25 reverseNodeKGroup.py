from ListNode import *

def reverseKGroup(head, k):
	head_copy = head
	def getLength(h):
		count = 0
		while h:
			count += 1
			h = h.next
		return count
	getLength(head_copy)