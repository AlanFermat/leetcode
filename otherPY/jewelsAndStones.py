def numJewelsInStones(J,S):
	n = len(S)
	count = 0
	for i in range(n):
		if S[i] in J:
			count += 1
	return count


J = "z"
S = "aZZ"
print numJewelsInStones(J,S)
			
