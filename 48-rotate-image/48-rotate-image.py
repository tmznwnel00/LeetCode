class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix)
        answer = []
        for i in range(x):
            temp = []
            for j in range(x-1, -1, -1):
                temp.append(matrix[j][i])
            answer.append(temp)
        for i in range(x):
            for j in range(x):
                matrix[i][j] = answer[i][j]