from binarySearch import binarySearch
def countOccurInSortedArr(seq, num):
	result = []
	start = 0
	end = len(seq)-1
	pos = binarySearch(seq, start, end, num)
	if pos >= 0:
		j = 0
		i = 0
		pos1 = pos2 = pos
		while pos1 >= 0:
			i = pos1
			pos1 = binarySearch(seq, start, pos1-1, num)
		while pos2 >0 and pos2 <= end:
			j = pos2
			pos2 =  binarySearch(seq, pos2+1, end, num)
		return j - i +1
	return 0

seq = [1]
num = 1
print countOccurInSortedArr(seq, num)