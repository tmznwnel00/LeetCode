class Solution:
    def concatenatedBinary(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
            b = len(bin(i))-2
            answer = (answer << b) + i
            answer %= (10**9 + 7)
        return answer % (10**9 + 7)