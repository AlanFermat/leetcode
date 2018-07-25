def  capital(word):
	if word == word.lower() or word == word.upper():
		return True
	elif word == word.title():
		return True
	else:
		return False

word = "DAA"
print capital(word)