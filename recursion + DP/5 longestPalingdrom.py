# find a longest palindrome substring in a string
# thoughts:
# use dynamic programming 
# o(n^2)
import numpy as np

def cal(a,b, s= 1):
	if s == 0:
		return 0
	else:
		if a == b:
			return 1
		return 0

def createMat(rowCount,colCount):
	mat = []
	for i in range (rowCount):
		rowList = []
		for j in range (colCount):
			rowList.append(0)
		mat.append(rowList)
	return mat

def longestPalindrome(string):
	n = len(string)
	table = createMat(n,n)
	start = 0
	end = 0
	maxLen = 1
	if n < 2:
		return string, n
	for i in range(n):
		table[i][i] = 1
	for i in range(n-1):
		table[i][i+1] = cal(string[i],string[i+1])
		if table[i][i+1] == 1:
			start = i 
			end = i + 1
			maxLen = 2 
	for i in range(n-2,-1,-1):
		for j in range(i+2,n):
			table[i][j] = cal(string[i],string[j],table[i+1][j-1])
			if table[i][j] == 1 and maxLen < j-i+1:
				maxLen = j-i+1
				start = i
				end = j
	return string[start:end+1], maxLen

print longestPalindrome("cadbbda")
