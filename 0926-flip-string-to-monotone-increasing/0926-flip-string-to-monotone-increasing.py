from collections import Counter
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt_1 = 0
        cnt_2 = Counter(s)['0']
        answer = cnt_1 + cnt_2
        for i in s:
            if i == '0':
                cnt_2 -= 1
            else:
                cnt_1 += 1
            m = cnt_1 + cnt_2
            answer = min(answer, m)
        
        return answer