import heapq
from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        answer = 0
        course = []
        indegree = defaultdict(set)
        outdegree = defaultdict(set)
        
        for relation in relations:
            indegree[relation[1]].add(relation[0])
            outdegree[relation[0]].add(relation[1])
            
        for index in range(n):
            if index + 1 not in indegree:
                heappush(course, [time[index], index + 1])

        while course:
            t, c = heappop(course)
            answer += t
            
            for lesson in course:
                lesson[0] -= t
            for degree in outdegree[c]:
                indegree[degree].remove(c)
                if len(indegree[degree]) == 0:
                    heappush(course, [time[degree - 1], degree])
                    del indegree[degree]
        return answer
        
            
        