from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        answer = 0
        for num in c:
            answer += c[num] * (c[num]-1) /2
            
            
        return int(answer)