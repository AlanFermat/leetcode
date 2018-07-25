def generate_int(N):
	for i in range(N):
		yield i


g = generate_int(10)
print g.next()
print g.next()
print g.next()

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list,3):
    print(c, value)