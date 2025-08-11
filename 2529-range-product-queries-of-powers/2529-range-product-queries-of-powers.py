import math
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        temp = 1
        answer = []
        while n:
            if n == 1:
                powers.append(1)
                break 
            if temp > n:
                temp /= 2
                n -= temp
                powers.append(int(temp))
                temp = 1
            else:
                temp *= 2
        powers.reverse()
        
        for x, y in queries:
            if x == y:
                answer.append(powers[x] % (10**9 + 7))
            else:
                answer.append(math.prod(powers[x:y+1]) % (10**9 + 7))
        return answer
            