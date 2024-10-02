class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        l = list(set(arr))
        l.sort()
        
        for i, n in enumerate(l):
            d[n] = i+1
            
        answer = []
        for a in arr:
            answer.append(d[a])
        
        return answer