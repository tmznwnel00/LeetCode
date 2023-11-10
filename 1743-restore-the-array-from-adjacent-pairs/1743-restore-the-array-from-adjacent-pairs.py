from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        for x, y in adjacentPairs:
            d[x].append(y)
            d[y].append(x)
            
        answer = []
        for key, value in d.items():
            if len(value) % 2 == 1:
                answer.append(key)
                break
        
        while len(answer) <= len(adjacentPairs):
            pop_val = d[answer[-1]].pop()
            d[pop_val].remove(answer[-1])
        
            answer.append(pop_val)
        
        return answer
            
            