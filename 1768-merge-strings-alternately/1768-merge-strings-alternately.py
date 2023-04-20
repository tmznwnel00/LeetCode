class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        leftover = min(len(word1), len(word2))
        for x, y in zip(word1, word2):
            answer += x
            answer += y
        answer += word1[leftover:]
        answer += word2[leftover:]
        return answer