from graph import *

numCourse = 3
course = [[1,0],[0,1],[2,0]]

def constructGraph(numCourse, course):
	g = Graph()
	for i in range(numCourse):
		g.add_edge(course[i][0],course[i][1])
	return g


g = constructGraph(numCourse,course)
print (g.nodes())




