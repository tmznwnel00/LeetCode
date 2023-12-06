class Solution:
    def totalMoney(self, n: int) -> int:
        quotient = n // 7
        remainder = n % 7
        
        answer = 0
        for i in range(quotient):
            answer += 28
            answer += 7*i
            
        for j in range(remainder):
            answer += j + quotient + 1
        
        return answer
        