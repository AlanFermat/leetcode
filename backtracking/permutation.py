def gen(nums):
	n = len(nums)
	if n == 0: yield tuple()
	else:
		for i in range(n):
			p = nums[i]
			for x in gen(nums[:i] + nums[i+1:]):
				yield tuple([p])+ x

def permute(nums):
	return list(gen(nums))



num = [1,1,3]
print permute(num)


def iter(data):
	for i in data:
		yield i

data = [1]
# print list(iter(data))



# print data[:0] + data[1:]s
