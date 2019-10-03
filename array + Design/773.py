from collections import deque

def solve(board):
	zero_pos = [0,0]
	final_state = [[1,2,3], [4,5,0]]
	next_moves = \
			{(0,0):[[0, 1], [1, 0]], 
			(0,1):[[0,0],[0,2],[1,1]], 
			(0,2):[[0,1], [1,2]], 
			(1,0):[[0,0],[1,1]], 
			(1,1):[[1,2], [1,0],[0,1]], 
			(1,2):[[1,1],[0,2]]}
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				zero_pos = [i,j]
	visited = set()
	visited.add(getState(board))
	q = deque()
	step = 0
	q.append((getState(board), zero_pos, step))
	while len(q) > 0:
		bd, zero_pos, step = q.popleft()
		if bd == getState(final_state):
			return step
		for next_move in next_moves[tuple(zero_pos)]:
			nextState = getBoard(bd)
			nextState[next_move[0]][next_move[1]], nextState[zero_pos[0]][zero_pos[1]] \
				= nextState[zero_pos[0]][zero_pos[1]], nextState[next_move[0]][next_move[1]]
			if getState(nextState) not in visited: 	
				visited.add(getState(nextState))
				q.append((getState(nextState), next_move, step + 1))
	return -1


def getState(board):
	return (board[0][0], board[0][1], board[0][2],\
		board[1][0], board[1][1], board[1][2])

def getBoard(state):
	board = [[],[],[]]
	for i in range(2):
		for j in range(3):
			board[i].append(state[j + i * 3])
	return board


board = [[1,2,3], [5,4,0]]

print (solve(board))



