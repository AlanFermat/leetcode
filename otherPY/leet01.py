import numpy as np 

d = dict()
li = [3,4,5,6,7]
target = 13

def twoSum(li,target):
	d = dict()
	for item in range(len(li)):
		index = []
		key = target - li[item]
		if key in d:
			index.append(d[key]+1)
			index.append(item+1)
		else:
			d[li[item]] = item
	return index

p = twoSum(li,target)
for i in p:
	print (i)

# d = dict()
# d[4] = 5
# d[5] = 6

# for i in d.values():
# 	print(i)
