import collections
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        pos = [0,0]
        dire = 2
        dist = 0
        dx = collections.defaultdict(set)
        dy = collections.defaultdict(set)
        for x,y in obstacles:
            dx[x].add(y)
            dy[y].add(x)
        for i in range(len(commands)):
            mov = commands[i]
            if mov < 0:
                dire = self.changeDir(dire, mov)
                continue
            for step in range(mov):
                if dire == 2:
                    candidate = [pos[0], pos[1] + 1]
                    if candidate[1] not in dx[pos[0]]:
                        pos = candidate
                    else:
                        break
                if dire == 4:
                    candidate = [pos[0], pos[1] - 1]
                    if candidate[1] not in dx[pos[0]]:
                        pos = candidate
                    else:
                        break
                if dire == 1:
                    candidate = [pos[0] + 1, pos[1]]
                    if candidate[0] not in dy[pos[1]]:
                        pos = candidate
                    else:
                        break
                if dire == 3:
                    candidate = [pos[0] - 1, pos[1] ]
                    if candidate[0] not in dy[pos[1]]:
                        pos = candidate
                        
                    else:
                        break
            dist = max(dist, pos[0] ** 2 + pos[1] ** 2)
        return dist
                
        
        
    def changeDir(self, dire, change):
        """
            Return a direction in the following coding:
                1: positive x
                3: negative x
                2: positive y
                4: negative y
        """
        if change == -1:
            dire -= 1
            if dire == 0:
                dire = 4
        if change == -2:
            dire += 1
            if dire == 5:
                dire = 1
        return dire
