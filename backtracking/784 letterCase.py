def letterCasePermutation(s):
	L = [[i.upper(),i.lower()] if i.isalpha() else [i] for i in s]
	res = ['']
	for j in range(len(L)):
		res = [p+k for p in res for k in L[j]]
	return res




s = "ab2h"
print letterCasePermutation(s)