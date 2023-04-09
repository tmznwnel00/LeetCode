class Solution:
    def partitionString(self, s: str) -> int:
        temp = ""
        answer = 0
        for letter in s:
            if letter not in temp:
                temp += letter
            else:
                answer += 1
                temp = letter
        return answer if temp == "" else answer + 1