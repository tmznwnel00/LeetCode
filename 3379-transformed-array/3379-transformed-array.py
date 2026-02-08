class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]

        for i, num in enumerate(nums):
            if num != 0:
                result[i] = nums[(i + num) % len(nums)]
                result[i] = nums[(i + num) % len(nums)]
            else:
                result[i] = nums[i]
        return result