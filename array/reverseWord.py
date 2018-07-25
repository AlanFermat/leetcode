def reverseWord(s):
	if not s:
		return ""
	if s:
		return " ".join(reversed(s.split()))


s = "life is    beautiful  get"
print reverseWord(s)