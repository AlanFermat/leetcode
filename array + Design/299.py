def solve(secret, guess):
	if not secret and not guess:
			return "0A0B"
	secret_map = {}
	for d in secret:
		secret_map[d] = secret_map.get(d, 0) + 1
	A = 0
	B = 0
	res = []
	for idx in range(len(guess)):
		if guess[idx] == secret[idx]:
			secret_map[guess[idx]] -= 1
			A += 1
			res.append(idx)
	for idx in range(len(guess)):
		if idx not in res and secret_map.get(guess[idx], 0) > 0:
			secret_map[guess[idx]] -= 1
			B += 1
	return str(A) + "A" + str(B) + "B"


secret = "1122"
guess = "1222"

print (solve(secret, guess))