class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        answer = 0
        for length, width in dimensions:
            if (length ** 2 + width ** 2) ** (1/2) > max_diagonal:
                max_diagonal = (length ** 2 + width ** 2) ** (1/2)
                answer = length * width
            elif (length ** 2 + width ** 2) ** (1/2) == max_diagonal:
                answer = max(length * width, answer)

        return answer