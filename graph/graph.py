class Graph:
    def __init__(self,mapping={}):
        '''
        Constructs a new empty graph. 
        '''
        
        self.graph = mapping

    def nodes(self):
        '''
        Returns a list of all nodes in the graph.
        '''
        return self.graph.keys()
    def get_neighbors(self, node):
        '''
        Given a particular node, returns a list of all neighbors in the graph. 
        '''
        return self.graph[node]
    def add_node(self, node):
        '''
        Adds the given node to the graph.  
        '''
        self.graph[node] = set()
    def add_edge(self, node1, node2):
        '''
        Adds an edge between the given pair of nodes, adding the nodes themselves first if they are not already in the graph. 
        '''
        if not node1 in self.graph.keys():
            self.add_node(node1)
        if not node2 in self.graph.keys():
            self.add_node(node2)
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)