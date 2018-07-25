def accountsMerge(accounts):
	"""
	:type accounts: List[List[str]]
	:rtype: List[List[str]]
	"""
	match = {}
	output =  []
	count = 0
	for i in range(len(accounts)):
		if accounts[i][0] not in match.keys():
			match[accounts[i][0]] = accounts[i][1:]
		else:
			flag  = False
			j = 1
			m = len(accounts[i])
			while j < m:
				if accounts[i][j] in match[accounts[i][0]]:
					flag = True
					accounts[i].remove(accounts[i][j])
					m -= 1
				else:
					j += 1
			if flag:
				match[accounts[i][0]] += accounts[i][1:]
			else:
				match[accounts[i][0] + ':'+str(count)] = accounts[i][1:]
				count += 1
	for name in match:
		temp = []
		idx = name.rfind(':')
		if idx == -1:
			temp.append(name)
			temp += match[name]
		else:
			temp += match[name]
			name = name[:idx]
			temp.insert(0, name)
		output.append(temp)
	return output


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

print (accountsMerge(accounts))
