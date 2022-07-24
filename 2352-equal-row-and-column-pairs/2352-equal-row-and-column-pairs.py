class Solution(object):
    def equalPairs(self, grid):
        col = []
        answer = 0
        for i in range(len(grid[0])):
            l = []
            for j in range(len(grid)):
                l.append(grid[j][i])
            col.append(l)
        for i in range(len(grid)):
            for j in range(len(col)):
                if grid[i] == col[j]:
                    answer += 1
        return answer