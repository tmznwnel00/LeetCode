class Solution(object):
    def minMoves2(self, nums):
        length = len(nums)
        nums = sorted(nums)
        temp = 0
        answer = 0
        if length % 2 == 1:
            temp = nums[length//2]
        else:
            temp = int(round((nums[length//2] + nums[length//2-1])/2))
            
        for i in range(length):
            answer += abs(nums[i] - temp)
        return answer
        