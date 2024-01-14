from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0

        for value in Counter(nums).values():
            while True:
                if value == 4:
                    answer += 2
                    break
                elif value in (2,3):
                    answer += 1
                    break
                elif value == 1:
                    return -1
                else:
                    value -= 3
                    answer += 1
        
        return answer