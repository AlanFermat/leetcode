from ListNode import *

def show(node):
	temp = []
	while node:
		temp.append(str(node.val))
		node = node.next
	print ("->".join(temp))

l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    output = dummy
    if not l1 and not l2:
        return 
    if not l1:
        return l2
    if not l2:
        return l1
    carry = 0 
    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        add = a + b + carry
        if add > 9:
            add = add % 10
            carry = (a+b+carry)//10
            dummy.next = ListNode(add)
        else:
            dummy.next = ListNode(add)
            carry = 0
        dummy = dummy.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    print (carry)
    if carry > 0 :
        dummy.next = ListNode(carry)
    return output.next

show(addTwoNumbers(l1,l2))



