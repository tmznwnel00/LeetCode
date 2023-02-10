import numpy as np
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        nomi = []
        nomi2 = []
        if np.sum(grid) == 0 or np.sum(grid) == n **2:
            return -1
        def cal(grid, x, y):
            if x + 1 < n and grid[x + 1][y] == 0:
                grid[x + 1][y] = 1
                nomi.append((x + 1, y))
            if x - 1 >= 0 and grid[x - 1][y] == 0:
                grid[x - 1][y] = 1
                nomi.append((x - 1, y))
            if y + 1 < n and grid[x][y + 1] == 0:
                grid[x][y + 1] = 1
                nomi.append((x, y + 1))
            if y - 1 >= 0 and grid[x][y - 1] == 0:
                grid[x][y - 1] = 1
                nomi.append((x, y - 1))
            return grid
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    nomi2.append((i, j))
        answer = -1
        while nomi == []:
            answer += 1
            while len(nomi2) > 0:
                x, y = nomi2.pop()
                cal(grid, x, y)
            nomi2 = nomi[:]
            if nomi == []:
                break
            else:
                nomi = list(())
        return answer