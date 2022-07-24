class Solution(object):
    def zeroFilledSubarray(self, nums):
        if nums.count(0) == 0:
            return 0
        
        answer = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                answer += count * (count + 1) / 2
                count = 0
            if i == len(nums) - 1:
                answer += count * (count + 1) / 2
        return answer