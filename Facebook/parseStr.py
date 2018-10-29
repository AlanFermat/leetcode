def encode(array):
	res = []
	for s in array:
		res.append(parseHelper(s))
	return ";".join(res)

def parseHelper(s):
	s_l = list(s)
	flag = False
	for item in s_l:
		if item == ";":
			flag = True
			break
	idx = 0
	n = len(s_l)
	while idx < n:
		if s_l[idx] == "\"":
			s_l[idx] = "\"\""
		idx += 1
	if flag:
		s_l.append("\"")
		s_l.insert(0, "\"")
	return "".join(s_l)
		

def check(l, idx):
	if l[idx] == "\"" :
		if l[idx-1] != "\"":
			return False, ""
		else:
			return True, "\""
	else:
		return True, l[idx]

def decode(string):
	res = []
	s_list = list(string)
	temp = ""
	while s_list:
		if s_list[-1] == '"':
			s_list.pop()
			idx = len(s_list) - 1
			while idx > 0:
				flag, val = check(s_list, idx)
				if not flag:
					break
				if val == '"':
					s_list.pop()
				s_list.pop()
				temp = val + temp 
				idx = len(s_list) - 1
			s_list.pop()
			res = [temp] + res
		else:
			while s_list and s_list[-1] != ";":
				temp = s_list.pop() + temp
			res = [temp] + res
		temp = ""
		if s_list:
			s_list.pop()
	return res


array = ["a;\"bc", "cde"]
print (encode(array))
print (decode(encode(array)))


