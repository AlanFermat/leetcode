def boat(people, limit):
	people = sorted(people)
	n = len(people)
	start, end = 0, n-1
	count = 0
	while start <= end:
		if people[start] + people[end] <= limit:
			count += 1
			start += 1
			end -= 1
		else:
			end -= 1
			count += 1
	return count

people = [3,4,2,2,5,2,1]
limit = 5
print (boat(people, limit))
			


