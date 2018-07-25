def isValid(A):
	stack = []
	for i in range(len(A)):
		if A[i] == '(' or A[i] == '[' or A[i] == '{':
			stack.append(A[i])
		if A[i] == ')':
			if not stack or stack.pop() != '(':
				return False
		if A[i] == ']':
			if not stack or stack.pop() != '[':
				return False
		if A[i] == '}':
			if not stack or stack.pop() != '{':
				return False
	if stack != []:
		return False
	return True

A = "([]{)}"
print isValid(A)