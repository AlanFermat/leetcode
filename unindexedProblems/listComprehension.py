evenNum = [x for x in range(10) if x%2 == 0]
evenSquares = [y**2 for y in range(10) if y % 2 == 0]
increasingPairs = [(x,y) 
					for x in range(10)
					for y in range(x+1,10)]
print increasingPairs

"""
enumerate iterate over item and index
"""
for index, item in enumerate(evenSquares):
	print index, item