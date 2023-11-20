from collections import Counter
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        answer = 0
        m,p,g = 0,0,0
        for i in range(len(garbage)-1, -1, -1):
            c = Counter(list(garbage[i]))
            if m == 0:
                if 'M' in c and i != 0:
                    answer += sum(travel[:i])
                    m = 1
            if p == 0:
                if 'P' in c and i != 0:
                    answer += sum(travel[:i])
                    p = 1
            if g == 0:
                if 'G' in c and i != 0:
                    answer += sum(travel[:i])
                    g = 1
            answer += sum(c.values())
            
        return answer
            