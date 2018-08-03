from ListNode import * 
def add(x, y):
	start = ListNode(-1)
	res= start
	values = [0]
	x1, x2= x, y
	m, n = 0, 0
	while x1:
		x1 = x1.next
		m += 1
	while x2:
		x2 = x2.next
		n += 1
	# make sure x is the longer
	if n > m:
		x, y, m ,n = y, x, n, m

	for i in range(m-n):
		values.append(x.val)
		x = x.next

	for _ in range(n):
		values.append(x.val + y.val)
		x, y = x.next, y.next

	for idx in range(len(values)-1, 0, -1):
		values[idx-1]= values[idx -1] + values[idx]/10
		values[idx] = values[idx] % 10
	for k in range(len(values)):
		start.next= ListNode(values[k])
		start = start.next
	if res.next.val == 0:
		return res.next.next
	return res.next









	

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(4)
# l1.next.next.next = ListNode(3)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(4)
print ( l1 == l2 )

show(add(l1, l2))


