class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        original = heights[:]
        while True:
            check = 0
            for i in range(len(heights) - 1):
                if heights[i] > heights[i + 1]:
                    check += 1
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
            if check == 0:
                break
        for i in range(len(heights)):
            if original[i] != heights[i]:
                answer += 1
        return answer