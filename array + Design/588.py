class TrieNode():
    def __init__(self):
        self.children = {}
        self.leaf = False

class FileSystem(object):

    def __init__(self):
        self.root = TrieNode()

        

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """