from collections import defaultdict as dd
class FreqStack(object):

	def __init__(self):
		self.highest = 0
		self.freq = dd(int)
		self.freqset = dd(list)
		

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.freq[x] += 1
		self.freqset[self.freq[x]].append(x)
		self.highest = max(self.highest,self.freq[x])
		

	def pop(self):
		"""
		:rtype: int
		"""
		out = self.freqset[self.highest].pop()
		self.freq[out] -= 1
		if not self.freqset[self.highest]:
			self.highest -= 1
		return out

l = FreqStack()
l.push(5)
l.push(7)
l.push(5)
l.push(7)
l.push(4)
l.push(5)
# print l.freqset.keys()[-1]
print l.pop()
# print l.freqset[l.freqset.keys()[-1]]
print l.pop()
print l.pop()
print l.pop()
print l.pop()
print l.freqset
print l.highest
l.push(5)
print l.freqset
print l.highest
print l.pop()
l.push(7)
l.push(9)
print l.freqset
print l.highest
print l.pop()
print l.pop()
print l.pop()








