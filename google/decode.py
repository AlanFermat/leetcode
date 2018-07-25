def encode(strs):
	"""Encodes a list of strings to a single string.
	
	:type strs: List[str]
	:rtype: str
	"""
	temp = ""
	for word in strs:
		temp += str(len(word)) + ':' + word
	return temp
	

def decode(s):
	"""Decodes a single string to a list of strings.
	
	:type s: str
	:rtype: List[str]
	"""
	out = []
	while s:
		idx = s.find(':')
		length = int(s[0:idx])
		part = s[idx+1:idx+length+1]
		out.append(part)
		s = s[idx+length+1:]
	return out

l = ["`H","HlJfc&48}:.#4?wQ;q",">wQvyT.%J].z4o;}t`r","icEM?,5pldc","`U#"," yS","2A6ukFJl","G"]
en = encode(l)
print en
print decode(en)

