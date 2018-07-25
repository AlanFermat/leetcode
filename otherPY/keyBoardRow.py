def findWords(words):
    line1 = set('qwertyuiop')
    line2 = set('asdfghjlkl')
    line3 = set('zxcvbnm')
    ans = []
    for string in words:
    	word = set(string.lower())
    	if word&line1 == word:
    		ans.append(string)
    	if word&line2 == word:
    		ans.append(string)
    	if word&line3 == word:
    		ans.append(string)
    return ans

words = ["Hello", "Alaska", "Dad", "Peace"]
print findWords(words)