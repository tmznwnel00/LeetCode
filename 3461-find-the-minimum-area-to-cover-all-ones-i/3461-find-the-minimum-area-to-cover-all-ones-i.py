class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_x, max_x, min_y, max_y = 1001, -1, 1001, -1

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                g = grid[x][y]
                if g:
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)
     
        return (max_x - min_x + 1) * (max_y - min_y + 1)