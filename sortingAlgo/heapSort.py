# Heap can be thought as a complete binary tree in which all the nodes are as far left as possible 
# https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees
# picture URL: https://en.wikipedia.org/wiki/File:Complete_binary.pdf

# Max Heap is a heap where parent node is always greater than or 
# equal to child nodes

# We compare the parent and child nodes, if parent < child, swap them
# After finishing the construction of Max heap
# swap the first and last node
# then delete the last nodes

# Algorithm ends when there is only one element left in the heap

def heapify(seq, n, i):
	l = 2 * i + 1
	r = 2 * i + 2
	largest =  i
	if l<n and seq[l] > seq[i]:
		largest = l
	if r<n and seq[r] > seq[largest]:
		largest = r
	if largest != i:
		seq[i], seq[largest] = seq[largest], seq[i]
		heapify(seq, n, largest)


def heapSort(seq):
	n = len(seq)
	for i in range(n, -1, -1):
		#for each step make a max heap from a triangle subtree from bottom up
		heapify(seq, n, i)
	for j in range(n-1, 0, -1):
		seq[0], seq[j] = seq[j], seq[0]
		heapify(seq, j,0)



seq = [4,10,3,5,1]
heapSort(seq)
print seq