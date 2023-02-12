class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) // 2):
            answer += int(str(nums[i]) + str(nums[-i - 1]))
        if len(nums) % 2 == 1:
            answer += nums[len(nums) // 2]
        return answer  