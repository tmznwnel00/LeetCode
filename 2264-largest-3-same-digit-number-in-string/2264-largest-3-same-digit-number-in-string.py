class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = 0
        
        for a,b,c in zip(num[:-2], num[1:-1], num[2:]):
            if a == b == c and int(a+b+c) >= int(answer):
                answer = a+b+c
        return "" if answer == 0 else answer