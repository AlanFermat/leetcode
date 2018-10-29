def pairsMatch(paira, pairb):
	m = {}
	for k, v in pairb:
		m[k] = v
	for k, v in paira:
		m[k] = v
	res = []
	for k, v in m.items():
		res.append([k, v])
	return res

a = [["x",10],["y",11]]
b = [["x",13],["z", 15],["x",20]]

print (pairsMatch(a, b))




