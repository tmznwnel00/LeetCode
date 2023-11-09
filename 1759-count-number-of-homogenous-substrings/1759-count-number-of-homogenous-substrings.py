class Solution:
    def countHomogenous(self, s: str) -> int:
        now = s[0]
        cnt = 1
        answer = 0
        def sigma(n):
            return n*(n+1)/2
        
        for c in s[1:]:
            if c == now:
                cnt += 1
            else:
                answer += sigma(cnt)
                cnt = 1
                now = c
                
        answer += sigma(cnt)
        
        return int(answer) % (10**9+7)
                