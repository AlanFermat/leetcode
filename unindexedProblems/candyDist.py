def candyDist(candies):
	candies.sort()
	start = 0
	count = 1
	print candies
	while count < len(candies)/2 and start < len(candies)-1:
	    if candies[start] != candies[start+1]:
	        count += 1
	    start += 1
	return count

candies = [1,2,3,2,1,2,3,4]
print candyDist(candies)