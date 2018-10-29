from collections import defaultdict as dd
def accountsMerge(accounts):
	"""
	:type accounts: List[List[str]]
	:rtype: List[List[str]]
	"""
	graph = dd(set)
	em_to_name = {}
	for acc in accounts:
		name = acc[0]
		for email in acc[1:]:
			graph[acc[1]].add(email)
			graph[email].add(acc[1])
			em_to_name[email] = name
	print (graph)
	seen = set()
	ans = []
	for email in graph:
		if email not in seen:
			seen.add(email)
			stack = [email]
			component = []
			while stack:
				node = stack.pop()
				component.append(node)
				for nbr in graph[node]:
					if nbr not in seen:
						seen.add(nbr)
						stack.append(nbr)
			ans.append([em_to_name[email]] + sorted(component))
	return ans


accounts = [["john","johnf@gmail.com"],["john","jjj@gmail.com","johnf@gmail.com","lokk@gmail.com","ccc@gmail.co"]]
print (accountsMerge(accounts))


