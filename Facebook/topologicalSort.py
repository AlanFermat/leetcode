def topoDfs(graph, n):
	v = {}
	for node in range(1, n+1):
		v[node] = 0
	stack = []
	for i in graph:
		if not v[i]:
			if not dfs(i, v, stack, graph):
				return False
	print (stack)
	return True

def dfs(i, v, stack, graph):
	if v[i] == -1:
		return False
	if v[i] == 1:
		return True
	v[i] = -1
	if graph.get(i, -10) != -10:
		for j in graph[i]:
			if v[j] != 1:
				if not dfs(j, v, stack, graph):
					return False
	stack.insert(0, i)
	v[i] = 1
	return True

# def topologicalSortUtil(self,v,visited,stack): 
  
#         # Mark the current node as visited. 
#         visited[v] = True
  
#         # Recur for all the vertices adjacent to this vertex 
#         for i in self.graph[v]: 
#             if visited[i] == False: 
#                 self.topologicalSortUtil(i,visited,stack) 
  
#         # Push current vertex to stack which stores result 
#         stack.insert(0,v) 
  
#     # The function to do Topological Sort. It uses recursive  
#     # topologicalSortUtil() 
# def topologicalSort(self): 
#     # Mark all the vertices as not visited 
#     visited = [False]*self.V 
#     stack =[] 

#     # Call the recursive helper function to store Topological 
#     # Sort starting from all vertices one by one 
#     for i in range(self.V): 
#         if visited[i] == False: 
#             self.topologicalSortUtil(i,visited,stack) 

#     # Print contents of the stack 
#     print stack 


graph = {4:[2,3],2:[3,1],5:[1,2,3,4]}

print (topoDfs(graph, 5))
