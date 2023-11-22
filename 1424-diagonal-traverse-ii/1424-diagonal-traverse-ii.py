from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        answer = []
        for i, num in enumerate(nums):
            for j in range(len(num)):
                d[i+j] = [num[j]] + d[i+j]
                
        for i in range(len(d)):
            for j in d[i]:
                answer.append(j)
        return answer