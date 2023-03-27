class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        if len(grid[0]) == 1 and len(grid) == 1:
            return grid[0][0]
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x - 1 <= -1:
                    dp[x][y] = dp[x][y-1]
                elif y - 1 <= -1:
                    dp[x][y] = dp[x-1][y]
                else:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1])
                dp[x][y] += grid[x][y]
        
        return dp[-1][-1]