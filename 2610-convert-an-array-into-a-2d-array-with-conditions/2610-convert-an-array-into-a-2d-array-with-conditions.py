class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        
        for num in nums:
            flag = 0
            for l in answer:
                if num not in l:
                    l.append(num)
                    flag = 1
                    break
            if not flag:
                answer.append([num])
        
        return answer
                    
            