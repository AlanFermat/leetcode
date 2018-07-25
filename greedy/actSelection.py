# select activity according to schedule to
# make a most compact activity schedule for students
def activity_select(start, finish):
	"""
	finish is a sorted list for time
	"""
	n = len(start)
	choice = []
	i = 0
	choice.append(i)
	for j in xrange(n):
		if start[j] >= finish[i]:
			i = j
			choice.append(i)
	return choice



start = [1 , 3 , 0 , 5 , 8 , 5]
finish = [2 , 4 , 6 , 7 , 9 , 9]
print activity_select(start, finish)