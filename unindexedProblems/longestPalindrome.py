def isPalingdrome(s):
	n = len(s)
	if n == 1 or n == 0 :
		return True
	if n == 2:
		return s[0] == s[1]
	if s[0] == s[n-1]:
		return isPalingdrome(s[1:n-1])
	if s[0] != s[n-1]:
		return False


def longestPalindrome(s):
	n = len(s)
	if isPalingdrome(s):
		return s
	else:
		if len(longestPalindrome(s[0:n-1])) > len(longestPalindrome(s[1:n]))


s =  "asbbhbb"
print longestPalindrome(s)