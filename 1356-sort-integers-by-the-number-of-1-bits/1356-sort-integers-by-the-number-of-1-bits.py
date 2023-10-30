from collections import Counter, defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for a in arr:
            d[Counter(bin(a))['1']].append(a)
        
        result = []
        
        for i in sorted(d.keys()):
            result.extend(sorted(d[i]))
            
        return result