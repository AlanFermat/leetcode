class FileSystem:

	def __init__(self):
		self.root = {"":{}}
		

	def createPath(self, path: str, value: int) -> bool:
		if not path or path == '/':
			return False
		nodes = path.split("/")
		root = self.root
		for node in nodes[:-1]:
			if node in root:
				root = root[node]
			else:
				return False
		if nodes[-1] in root:
			return False
		else:
			root[nodes[-1]] = {"#":value}
			return True

	def get(self, path: str) -> int:
		if not path or path == '/':
			return -1
		nodes = path.split('/')
		root = self.root
		for node in nodes:
			if node in root:
				root = root[node]
			else:
				return -1
		return root['#']



fs = FileSystem()
print(fs.createPath("/leet", 1))
print(fs.createPath("/leet/code", 2))
print(fs.createPath("/leet/code", 3))
print(fs.get("/leet"))
print(fs.get("/leet/code"))
print(fs.createPath("/c/d", 3))
print(fs.get("/c/d"))







