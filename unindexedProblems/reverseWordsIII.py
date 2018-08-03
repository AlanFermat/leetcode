input1 = input()
def reverseWords(input):
	words = input.split()
	print (words)
	ans = []
	for word in words:
		word_reversed = list(word)
		word_reversed.reverse()
		result = "".join(word_reversed)
		ans.append(result)
	ans = " ".join(ans)
	return ans


print (reverseWords(input1))