from collections import defaultdict as dd
def countOfAtoms(formula):
	curr_data = dd(int)
	stack = []
	idx = 0
	n = len(formula)
	curr_element = ""
	curr_num = 1
	while idx < n:
		if formula[idx].isupper():
			if curr_element:
				curr_data[curr_element] += curr_num
			curr_element = formula[idx]
			curr_num = 1
		elif formula[idx].islower():
			curr_element += formula[idx]
		elif formula[idx].isdigit():
			if formula[idx-1].isdigit():
				curr_num = curr_num * 10 + int(formula[idx])
			else:
				curr_num = int(formula[idx])
		elif formula[idx] == "(":
			if curr_element:
				curr_data[curr_element] += curr_num
			stack.append(curr_data)
			curr_element = ""
			curr_num = 1
			curr_data = dd(int)

		elif formula[idx] == ")":
			if curr_element:
				curr_data[curr_element] += curr_num
			idx += 1
			num = 0
			while idx < len(formula) and formula[idx].isdigit():
				if formula[idx-1].isdigit():
					num = num * 10 + int(formula[idx])
				else:
					num = int(formula[idx])
				idx += 1
			if not num:
				num = 1
			idx -= 1
			prev_data = stack.pop()
			for element in curr_data:
				curr_data[element] *= num
			if len(prev_data) > 0:
				for key in curr_data:
					if key in prev_data:
						prev_data[key] += curr_data[key]
					else:
						prev_data[key] = curr_data[key]
				curr_data = prev_data
			curr_element = ""
			curr_num = 1
		idx += 1
	if curr_element:
		curr_data[curr_element] += curr_num
	elements = sorted(curr_data.keys())
	res = ""
	for e in elements:
		if curr_data[e] >1 :
			res = res + e + str(curr_data[e])
		else:
			res += e
	return res

formula = "((H4)2((O)4)4)"
print (countOfAtoms(formula))


