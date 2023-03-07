import numpy as np
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = min(time) * totalTrips

        while l < r:
            m = (l + r) // 2
            
            temp = 0
            for t in time:
                temp += m // t
            if temp >= totalTrips:
                r = m
            else:
                l = m + 1
            
        return l