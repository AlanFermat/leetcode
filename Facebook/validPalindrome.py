import string, re
def valid(s):
	temp = re.sub("[" + string.punctuation + "]", "",s)
	temp = temp.replace(" ", "").lower()
	return temp[::-1] == temp

s = "A man, a plan, a canal: Panama"
print (valid(s))
	