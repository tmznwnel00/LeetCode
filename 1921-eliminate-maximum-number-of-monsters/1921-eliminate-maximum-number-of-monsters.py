import math
import heapq
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reach = []
        
        for d, s in zip(dist, speed):
            heapq.heappush(reach, math.ceil(d/s))
        
        answer = 0
        for i in range(len(dist)):
            monster = heapq.heappop(reach)
            if monster <= i:
                return answer
            else:
                answer += 1
            
        return answer