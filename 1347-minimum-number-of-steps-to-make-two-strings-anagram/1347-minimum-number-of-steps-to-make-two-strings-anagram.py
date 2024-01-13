from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        now = 0
        for c in s_count.keys():
            if c in t_count:
                now += min(t_count[c], s_count[c])
        
        return len(s) - now