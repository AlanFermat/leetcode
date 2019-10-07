def solve(info, pageSize):
	res = []
	if not info:
		return res
	n = len(info)
	visited = {}
	idx = 0
	hosts = set()
	count = 0
	ttl_size = 0
	reachEnd = False
	while True:
		cur = info[idx]
		if visited.get(cur, 1) != 0:
			host_id = (cur.split(","))[0]
			if host_id not in hosts or reachEnd:
				visited[cur] = 0
				hosts.add(host_id)
				res.append(cur)
				count += 1
				ttl_size += 1
				if ttl_size == n:
					break
			if count == pageSize:
				res.append(" ")
				count = 0
				hosts = set()
				idx = 0
			if idx == n - 1:
				reachEnd = True
				idx = 0
			else:
				idx += 1
		else:
			idx = 0 if idx == n - 1 else idx + 1
	return res



info0 = ["1,28,310.6,SF",
        "4,5,204.1,SF",
        "20,7,203.2,Oakland",
        "6,8,202.2,SF",
        "6,10,199.1,SF",
        "1,16,190.4,SF",
        "6,29,185.2,SF",
        "7,20,180.1,SF",
        "6,21,162.1,SF",
        "2,18,161.2,SF",
        "2,30,149.1,SF",
        "3,76,146.2,SF",
        "2,14,141.1,San Jose"]

info = [ "1,28,300.1,SanFrancisco",
        "4,5,209.1,SanFrancisco",
        "20,7,208.1,SanFrancisco",
        "23,8,207.1,SanFrancisco",
        "16,10,206.1,Oakland",
        "1,16,205.1,SanFrancisco",
        "6,29,204.1,SanFrancisco",
        "7,20,203.1,SanFrancisco",
        "8,21,202.1,SanFrancisco",
        "2,18,201.1,SanFrancisco",
        "2,30,200.1,SanFrancisco",
        "15,27,109.1,Oakland",
        "10,13,108.1,Oakland",
        "11,26,107.1,Oakland",
        "12,9,106.1,Oakland",
        "13,1,105.1,Oakland",
        "22,17,104.1,Oakland",
        "1,2,103.1,Oakland",
        "28,24,102.1,Oakland",
        "18,14,11.1,SanJose",
        "6,25,10.1,Oakland",
        "19,15,9.1,SanJose",
        "3,19,8.1,SanJose",
        "3,11,7.1,Oakland",
        "27,12,6.1,Oakland",
        "1,3,5.1,Oakland",
        "25,4,4.1,SanJose",
        "5,6,3.1,SanJose",
        "29,22,2.1,SanJose",
        "30,23,1.1,SanJose"]

pageSize = 5


res = solve(info0, pageSize)
# for r in res:
# 	print(r)
print(len(res))
print(res[5])
print(res[14])








