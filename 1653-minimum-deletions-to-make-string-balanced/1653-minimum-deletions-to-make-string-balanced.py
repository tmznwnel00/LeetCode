class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_cnt, b_cnt = 0, 0
        for c in s:
            if c == 'a':
                a_cnt += 1
            else:
                b_cnt += 1
        
        l_b, r_a = 0, a_cnt
        answer = min(a_cnt, b_cnt)
        
        for i in range(len(s)):
            if s[i] == 'a':
                r_a -= 1
            else:
                l_b += 1
            if l_b + r_a < answer:
                answer = l_b + r_a
        return answer
                
            