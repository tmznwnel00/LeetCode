from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1 = dict(Counter(s))
        c2 = dict(Counter(goal))
        c3 = 0
        if c1 == c2:
            for x, y in zip(s, goal):
                if x != y:
                    c3 += 1
            if c3 == 2:
                return True
            elif c3 == 0 and max(c1.values()) >= 2:
                return True
            
        return False