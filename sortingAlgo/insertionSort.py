def insertionSort(seq, n):
	for i in range(1,n):
		element = seq[i]
		j = i - 1
		while j >= 0 and seq[j] > element:
			seq[j+1], seq[j] = seq[j], seq[j+1]
			j -= 1

seq = [10,8,7,6,2]
n = len(seq)
insertionSort(seq, n)
print seq
