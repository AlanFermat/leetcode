from Queue import PriorityQueue as pq

p = pq()
p.put((10,"e"))
p.put((15,"r"))
p.put((1,"t"))
while not p.empty():
	print p.get()
print p.empty()
