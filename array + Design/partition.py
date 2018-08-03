def partitionLabels(s):
	"""
	:type S: str
	:rtype: List[int]
	"""
	n = len(s)
	res = [[]]
	maxidx = 0
	for i in range(n):
		if i > maxidx:
			res.append([s[i]])
			maxidx = s.rfind(s[i])
		else:
			res[-1].append(s[i])
			maxidx = max(maxidx, s.rfind(s[i]))
	output = []
	for j in range(len(res)):
		output.append(len(res[j]))
	return output

			

S = "ababcbacadefegdehijhklij"
print (partitionLabels(S))