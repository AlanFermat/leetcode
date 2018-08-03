def findDuplicatePath(path):
	mapping = {}
	for i in range(len(path)):
		temp = path[i]
		temp = temp.split()
		mapping[temp[0]] = {}
		for j in range(1,len(temp)):
			op = temp[j].split("(")
			mapping[temp[0]][op[0]] = op[1]
	m = reverse(mapping)
	output = []
	for key in m:
		output.append(m[key])
	return output

def reverse(mapping):
	m = {}
	for key in mapping:
		for key1 in mapping[key]:
			m[mapping[key][key1]] = m.get(mapping[key][key1], []) + [key + '/' + key1]
	return m

path = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print (findDuplicatePath(path))
