from collections import defaultdict as dd

class FileSystem(object):

    def __init__(self):
       self.root = dd(dict)
        

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path == '/':       
            return list(self.root[''].keys())
        path_list = self.split_path(path)        
        root = self.root
        for node in path_list:
            root = root[node]
        if '#' in root:
            return [path_list[-1]]
        return list(root.keys())

        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        root = self.root
        if path == '/':
            if '' not in root:
                root[''] = {}
            return 
        path_list = self.split_path(path)
        for node in path_list:
            if node not in root:
                root[node] = {}
            root  = root[node]

        

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        root = self.root
        if filePath == '/':
            root['']['#'] = root[''].get('#', "") + content
        path_list = self.split_path(filePath)
        for node in path_list:
            if node not in root:
                root[node] = {}
            root = root[node]
        root['#'] = root.get('#', "") + content

        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        root = self.root
        if filePath == '/':
            return root['']['#']
        path_list = self.split_path(filePath)
        for node in path_list:
            root = root[node]
        return root['#']


    def split_path(self, path):
        return path.split('/')


fs = FileSystem()

fs.mkdir("/a/b/c")
fs.mkdir("/a/d/c")
fs.mkdir("/a/b/f")
fs.mkdir("/p/q/r/s")
fs.mkdir('/')
fs.addContentToFile('/a/b/c/file1', 'hello')
fs.addContentToFile('/a/b/c/file1', 'helloworld')
fs.addContentToFile('/a/d/c/file2', 'hell')
fs.addContentToFile('/a/k/i/file3', 'yo')
print (fs.root[''])
# print (fs.ls("/"))
# print (fs.root)





