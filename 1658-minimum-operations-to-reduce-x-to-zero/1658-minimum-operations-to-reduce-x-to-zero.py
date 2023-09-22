class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        right = 0
        temp = nums[0]
        answer = -1
        if len(nums) == 1:
            if nums[0] == x:
                return 1
            else:
                return -1
        while True:
            if left == len(nums) or right == len(nums):
                    break
            if temp < target:
                right += 1
                if right == len(nums):
                    break
                temp += nums[right]
            elif temp > target:
                temp -= nums[left]
                left += 1
            else:
                answer = max(answer, right - left + 1)
                temp -= nums[left]
                left += 1
                

        
        
        return answer if answer == -1 else len(nums) - answer 
            
                
        
            
            
            
        
        
        
        