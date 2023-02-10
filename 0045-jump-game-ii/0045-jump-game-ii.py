class Solution:
    def jump(self, nums: List[int]) -> int:
        temp = [len(nums)] * len(nums)
        temp[0] = 0
        for index, value in enumerate(nums):
            for k in range(1, value + 1):
                if index + k >= len(nums):
                    continue
                else:
                    temp[index + k] = min(temp[index + k], temp[index] + 1)
        return temp[-1]