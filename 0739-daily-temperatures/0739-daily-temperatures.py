class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for i in range(len(temperatures))]
        for index, temperature in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(index)
            else:
                while len(stack) > 0 and temperatures[stack[-1]] < temperature:
                    before = stack.pop()
                    answer[before] = index - before
                stack.append(index)
        return answer 