class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        now = nums[0]
        for i in range(1, len(nums)):
            now = max(now + nums[i], nums[i])
            answer = max(now, answer)
        return answer