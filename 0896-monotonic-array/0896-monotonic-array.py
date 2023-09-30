class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = 0
        for i, num in enumerate(nums[:-1]):
            if flag == 1:
                if num > nums[i+1]:
                    return False
            elif flag == -1:
                if num < nums[i+1]:
                    return False
            else:
                if num > nums[i+1]:
                    flag = -1
                elif num < nums[i+1]:
                    flag = 1
                else:
                    continue
                    
            
        return True
            