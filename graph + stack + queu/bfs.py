import sys
# how to import a file from another dir
sys.path.insert(0,'/Users/Alan/Desktop/SublimePython/')
from Queue import Queue
from graph import Graph
import matplotlib.pyplot as plt 
from collections import defaultdict
import numpy as np 

# Performs a breadth-first search on graph starting at the 
# start_node.

# Returns a two-element tuple containing a dictionary
# associating each visited node with the order in which it 
# was visited and a dictionary associating each visited node 
# with its parent node.
    
def bfs(graph, start_node):
    queue = Queue()
    dist = {}
    parent = {}
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    dist[start_node] = 0
    queue.push(start_node)
    while queue.items:
        node = queue.pop()
        for nbr in graph.get_neighbors(node):
            if dist[nbr] == float("inf"):
                dist[nbr] = dist[node] + 1
                parent[nbr] = node
                queue.push(nbr)
    return dist, parent

def distance_histogram(graph, node):
    """
    Given a graph and a node in that graph, returns a histogram
    (in the form of a dictionary mapping distance to counts) of
    the distances from node to every other node in the graph.
    """
    dist_dict = defaultdict(int)
    dist, _ = bfs(graph, node)
    for value in dist.values():
        dist_dict[value] += 1 
    dist_dict = dict(dist_dict)
    objects= dist_dict.keys()
    x_pos =  np.arange(len(objects))
    plt.bar(x_pos,dist_dict.values(), align = 'center', alpha = 0.5)
    
    plt.xlabel('distance')
    plt.ylabel('count of nodes')
    plt.xticks(x_pos, objects)
    plt.title('counting of nodes that have certia distance to the start_node')
    plt.show()

g = Graph()
g.add_node(3)
g.add_node(9)
g.add_node(7)
g.add_node(8)
g.add_node(10)
g.add_node(11)
g.add_edge(3,9)
g.add_edge(8,9)
g.add_edge(3,10)
g.add_edge(9,7)
g.add_edge(9,11)
distance_histogram(g, 10)
