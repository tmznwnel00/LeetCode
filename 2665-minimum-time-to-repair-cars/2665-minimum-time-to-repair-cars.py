import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, cars * cars * max(ranks)

        while l < r:
            m = (l + r) // 2
            temp = 0
            for rank in ranks:
                temp += math.floor(math.sqrt(m / rank))
            if temp < cars:
                l = m + 1
            else:
                r = m
        
        return (l + r) // 2