def simplifyPath(path):
	"""
	:type path: str
	:rtype: str
	"""
	s =  []
	path_list = path.split("/")
	print (path_list)
	for p in path_list:
		if p:
			if p == ".":
				continue
			elif p == "..":
				if not s:
					s.append("/")
				else:
					s.pop()
			else:
				s.append(p)
	res = ""
	for p in s:
		if p == "/":
			res += p
		else:
			res += "/"
			res += p
	return res
path = "/.."
print (simplifyPath(path))