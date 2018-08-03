class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        record = [[0 for _ in range(n)] for _ in range(m)] # record how many buildings can be reached from
            #this position of 0
        dist = [[0 for _ in range(n)] for _ in range(m)] # record the distance toward the position i ,j 
            # only record this if position i,j is 0
        total_building = sum(grid[i][j] for i in range(m) for j in range(n) if grid[i][j] == 1)
        # total number of buildings
        def bfs(start_x, start_y):
            """
                This is bfs for visiting the graph
            """
            count = 1 # if we can not connect all the buildings, we definitely can not
                # reach all of them by visiting, return -1
            visit = [[False for _ in range(n)] for _ in range(m)]
            q = [[start_x, start_y,0]]
            visit[start_x][start_y] = True
            while q:
                x, y, distance = q.pop(0)
                for i, j in (x+1,y), (x-1, y), (x, y+1), (x, y-1):
                    if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                        visit[i][j] = True
                        if grid[i][j] == 1:
                            count += 1
                        elif grid[i][j] == 0:
                            dist[i][j] += distance + 1
                            record[i][j] += 1
                            q.append([i,j,distance + 1])                
            return count == total_building
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    if not bfs(i,j):
                        return -1
        min_d = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and record[i][j] == total_building:
                    min_d = min(dist[i][j], min_d)
        if min_d == float('inf'):
            return -1
        return min_d
        
                    
                    
        
