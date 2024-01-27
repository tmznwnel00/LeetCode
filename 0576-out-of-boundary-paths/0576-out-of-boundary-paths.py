class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        matrix = [[[-1 for i in range(maxMove)] for j in range(n)] for k in range(m)]
        if maxMove:
            matrix[startRow][startColumn][0] = 1
        def dp(i, j, step):
            if i == startRow and j == startColumn and step == 0:
                return 1
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if matrix[i][j][step] != -1:
                return matrix[i][j][step]
            if step <= 0:
                return 0
            result = dp(i-1, j, step-1) + dp(i+1, j, step-1) + dp(i, j-1, step-1) + dp(i, j+1, step-1)
            matrix[i][j][step] = result
            return result
        
        answer = 0
        visited = set([])
        for i in range(m):
            visited.add((i, 0))
            visited.add((i, n-1))
        for j in range(n):
            visited.add((0, j))
            visited.add((m-1, j))
            
        d = {}
        for z in range(maxMove):
            for x, y in visited:
                temp = 0
                if (x, y) in d:
                    temp = d[(x, y)]
                else:
                    if x - 1 == -1:
                        temp += 1
                    if x + 1 == m:
                        temp += 1
                    if y - 1 == -1:
                        temp += 1
                    if y + 1 == n:
                        temp += 1
                answer += dp(x, y, z) * temp
        return answer % (10**9 + 7)
            