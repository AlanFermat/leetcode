import re, string
def valid(s):
	temp = re.sub("["+string.punctuation+"]","",s)
	temp = temp.replace(" ","")
	temp = temp.lower()
	return temp[::-1]  == temp
	

s = "A man, a plan, a canal: Panama"
print (valid(s))