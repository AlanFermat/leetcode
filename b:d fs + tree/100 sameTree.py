from binaryTree import Node

t1 = Node(1)
t1.left = Node(2)
t1.right = Node(3)

t2 = Node(1)
t2.left = Node(2)
t2.right = Node(3)


def treeToList(t):
	if t == None:
		return []
	result = [t.val]
	return result + treeToList(t.left) + treeToList(t.right)

def isSameTree(t,s):
	t_list = treeToList(t)
	s_list = treeToList(s)
	return s_list == t_list

def isSame(t,s):
	if not t and not s:
		return True
	if t and s:
		if t.val == s.val:
			return isSame(t.left, s.left) and isSame(t.right, s.right)
	return False
print (isSame(t1,t2))