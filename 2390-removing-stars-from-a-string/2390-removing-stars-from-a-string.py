class Solution:
    def removeStars(self, s: str) -> str:
        pointer = 0
        while pointer < len(s):
            if s[pointer] == '*':
                s = s[:pointer - 1] + s[pointer + 1:]
                pointer -= 1
            else:
                pointer += 1
        return s