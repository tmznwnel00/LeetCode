class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        
        while l < r:
            time = 0
            m = (l + r) // 2
            if m == 0:
                return 1
            for p in piles: 
                if p % m == 0:
                    time += p // m
                else:
                    time += p // m + 1
            if time <= h:
                r = m
            else:
                l = m + 1
        return l