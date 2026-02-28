from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in arr:
            d[bin(i)[2:].count('1')].append(i)
    
        answer = []
        
        for value in [sorted(v) for k, v in sorted(d.items())]:
            answer += value
        return answer

        
