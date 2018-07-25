def longestPath(input):
	paths = input.split('\n')
	counter, max_length = 0, 0
	s = []
	for p in paths:
		idx = p.rfind('\t')
		if idx == -1:
			depth = 1
		if idx != -1:
			depth = idx + 2
		p = p[idx+1:]

		# we store the counter for recyling 
		# so that we can count the number of words for
		# the length of next word in the paths
		while s and depth <= len(s):
			res = s.pop()
			counter -= len(res)
		s.append(p)
		counter += len(p)
		if p.rfind('.') != -1:
			c = len(s)
			max_length = max(max_length, c + counter - 1)
	return max_length

print len("dir/subdir2/file.ext")
print len("dir/subdir2/subsubdir2/file2.ext")
# input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print longestPath(input)



