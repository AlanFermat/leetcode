from ListNode import *

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

def split(root, k):
	ans = []
	r = root
	length = 1
	while r.next:
		r = r.next
		length += 1
	unit = length/k
	remain = length % k
	curr = root
	# we have k slots in total
	for i in range(k):
		head = write = ListNode(None)
		for j in range(unit + (remain > i)):
			write.next = ListNode(curr.val)
			write = write.next
			if curr:
				curr = curr.next
		ans.append(head.next)		
	return ans
	


l = split(root, 5)
for ll in l:
	show(ll)


	