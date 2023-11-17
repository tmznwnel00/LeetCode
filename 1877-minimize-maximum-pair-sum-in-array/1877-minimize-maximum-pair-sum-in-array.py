class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i in range(len(nums)//2):
            if nums[i] + nums[-i-1] > answer:
                answer = nums[i] + nums[-i-1]
        return answer
                