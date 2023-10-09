class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        answer = [-1, -1]
        l_check, r_check = False, False
        while l <= r:
            if nums[l] == target:
                answer[0] = l
                l_check = True
            elif nums[l] > target:
                break
            else:
                l += 1
            if nums[r] == target:
                answer[1] = r
                r_check = True
            elif nums[r] < target:
                break
            else:
                r -= 1
            
            if l_check and r_check:
                break
                
        return answer