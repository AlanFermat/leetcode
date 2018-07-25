# Sorting the elements with the range from 1 to n2
# note that counting sort will take O(n2 + n) = O(n2) on this and any other
# sorting algorithms can perform no better than O(n logn)
# yet this is a linear time solution

# most efficient when we sort an array range from 1 to n^c under the base n


# we use division here so that when there is no previous digit before 
# some number in the sequence here, we will automatically get zero

def countingSort(seq, diviser):
	n = len(seq)
	output = [0] * n
	countingBlock = [0] * 10
	for i in range(n):
		remains = seq[i]/diviser
		countingBlock[remains%10] += 1

	# construct the counting block
	for pos in range(9):
		countingBlock[pos+1] += countingBlock[pos]

	# Build the output array
	# use while from the last to the first because we want to
	# make sure in the generated sequence,
	# the order is preserved for the original position
	i = n-1
	while i>=0:
		remains = seq[i]/diviser
		output[ countingBlock[ remains%10 ] - 1] = seq[i]
		countingBlock[ remains%10 ] -= 1
		i -= 1

    # Copying the output array to seq[],
    # so that arr now contains sorted numbers

    # and we can not assign the whole output to the sequence
    # because we do not want to mess up with Ids of the two sequences
	for k in range(n):
		seq[k] = output[k]









def radixSorting(seq):
	max_num = max(seq)
	diviser = 1
	while max_num/diviser > 0:
		countingSort(seq, diviser)
		diviser *= 10
	return seq





seq = [1,29,182,840,299,30111,382,18,22222,1999]
print radixSorting(seq)

