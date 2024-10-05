class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        answer = 0
        for i in range(k):
            h = happiness.pop()
            if h-i < 0:
                break
            answer += (h-i)
            
        return answer