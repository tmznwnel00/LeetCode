class Solution:
    def countKeyChanges(self, s: str) -> int:
        last = s.lower()[0]
        answer = 0
        for c in s.lower()[1:]:
            if last != c:
                answer += 1
            last = c
            
        return answer