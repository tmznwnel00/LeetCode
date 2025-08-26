int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    double max_diagonal = 0;
    int answer = 0;

    for (int i=0; i<dimensionsSize; i++) {
        int length = dimensions[i][0];
        int width = dimensions[i][1];
        double diag = sqrt((pow(length, 2) + pow(width, 2)));
        
        if (diag > max_diagonal) {
            max_diagonal = diag;
            answer = length * width;
        } else if (diag == max_diagonal) {
            if (length * width > answer) {
                answer = length * width;
            }
        }
    }

    return answer;
}