from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        now_c = None
        now_s = ""
        d = defaultdict(int)
        for c in s:
            if c != now_c:
                now_c = c
                now_s = c
                d[now_s] += 1
            else:
                now_s += c
                for i in range(len(now_s)):
                    d[now_c * (i + 1)] += 1
        
        answer = -1
        for key, val in d.items():
            if val >= 3 and len(key) > answer:
                answer = len(key)
        
        return answer
            
            