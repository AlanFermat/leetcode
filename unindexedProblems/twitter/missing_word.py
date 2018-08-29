def missingWords(s, t):
	"""
	Input: s - a string
		   t - a string, also a subsequence of s
	Return: miss_words - an array of missing words in exact order as in s
	"""
	s_word_list = s.split(" ")
	t_word_list = t.split(" ")
	s_len, t_len = len(s_word_list), len(t_word_list)
	miss_words = []
	idx_s, idx_t = 0, 0
	while idx_s < s_len and idx_t < t_len:
		if s_word_list[idx_s] == t_word_list[idx_t]:
			idx_s += 1
			idx_t += 1
		else:
			miss_words.append(s_word_list[idx_s])
			idx_s += 1
	while idx_s < s_len:
		miss_words.append(s_word_list[idx_s])
		idx_s += 1
	return miss_words

s = ""
t = ""

print missingWords(s,t)

