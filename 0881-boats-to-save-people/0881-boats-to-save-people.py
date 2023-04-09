class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        answer = 0
        for p in people:
            if p + people[-1] <= limit:
                people.pop()
            answer += 1
        
        return answer
        