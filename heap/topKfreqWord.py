from heapq import *
from collections import defaultdict as dd

def sol(arr, k):
	h = []
	d = dd(int)
	for word in arr:
		d[word] += 1
	



arr = ["i","love","love","leet","leet","code","i","code","love"]