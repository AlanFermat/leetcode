# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#reverse
#[5,7,3]
#[2,4,1]
#in order 
#[5,1,7]




h = ListNode(5)
l = ListNode(5)
h.next = ListNode(9)
h.next.next = ListNode (1)
h.next.next.next = ListNode(2)


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    store = curr = ListNode(-1)
    carry = 0
    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        summ = a + b + carry 
        curr.next = ListNode(summ%10)
        curr = curr.next
        carry = summ //10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        if carry > 0:
        	curr.next = ListNode(1)
    return store.next 

def reverseRecursive(head):
	curr = head
	if curr == None:
		return 
	else:
		if curr.next == None:
			head = curr
		else:
			head = reverseRecursive(curr.next)
			curr.next.next = curr
			curr.next = None
	return head






f = reverseRecursive(h)
while f:
	print(f.val)
	f = f.next


# f = addTwoNumbers(h,l)
# while f:
# 	print (f.val)
# 	f = f.next

