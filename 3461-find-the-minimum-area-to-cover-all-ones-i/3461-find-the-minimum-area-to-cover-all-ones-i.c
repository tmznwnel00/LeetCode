int minimumArea(int** grid, int gridSize, int* gridColSize) {
    int min_x = 1001;
    int max_x = -1;
    int min_y = 1001;
    int max_y = -1;

    for (int x = 0; x < gridSize; x++) {
        for (int y = 0; y < *gridColSize; y++) {
            if (grid[x][y]) {
                if (x < min_x) min_x = x;
                if (x > max_x) max_x = x;
                if (y < min_y) min_y = y;
                if (y > max_y) max_y = y;
            }
        }
    };

    return (max_x - min_x + 1) * (max_y - min_y + 1);
}