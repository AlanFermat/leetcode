def textQueries(sentences, queries):
	"""
		Input: sentences - an array of strings 
			   queries - an array of strings to be matched in sentences
		Return: match_result - an array of arrays, where match_result[i] denotes an array
							   of indices for sentences that contain all words in queries[i]
	"""
	match_result = []
	queries_len = len(queries)
	sentence_content = {}

	# store the contents (word, its occurrence times) mapping of each sentence
	for idx, sentence in enumerate(sentences):
		word_list = sentence.split(" ")
		sentence_content[idx] = {}
		for word in word_list:
			sentence_content[idx][word] = sentence_content[idx].get(word, 0) + 1

	def check(word_query_map, one_sentence):
		"""
			This function check if all words in query are in this sentence
		"""
		for word in word_query_map:
			if word_query_map[word] > one_sentence.get(word,0):
				return False
		return True
	# for each query check if its words are contained in the sentence
	for query in queries:
		match = []
		word_query = query.split(" ")
		word_query_map = {}
		for word_to_find in word_query:
			word_query_map[word_to_find] = word_query_map.get(word_to_find, 0) + 1

		for idx in sentence_content: 	
			if check(word_query_map, sentence_content[idx]):
				match.append(idx)
		print " ".join(list(map(lambda x: str(x),match)))



sentences = ["jim likes mary","kate likes tom","tom does not like jim"]
queries = ["jim tom", "likes"]
textQueries(sentences, queries)






