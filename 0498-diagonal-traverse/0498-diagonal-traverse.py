class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        cnt = 0
        answer = []

        for k in range(len(mat) + len(mat[0])):
            if k % 2 == 0:
                i, j = min(len(mat) - 1, k), max(0, k - len(mat) + 1)
            else:
                i, j = max(0, k - len(mat[0]) + 1), min(len(mat[0]) - 1, k)
            for s in range(k + 1):
                if i >= 0 and i <= len(mat) - 1 and j >= 0 and j <= len(mat[0]) - 1:
                    answer.append(mat[i][j])
                else:
                    break

                if k % 2 == 0:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            

        return answer


        


