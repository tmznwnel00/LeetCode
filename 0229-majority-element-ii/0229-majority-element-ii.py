from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []
        
        length = len(nums)
        c = Counter(nums)
        
        for key, value in c.items():
            if value > length//3:
                answer.append(key)
        return answer
        