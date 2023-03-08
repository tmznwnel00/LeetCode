class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_index = nums[i:].index(min(nums[i:])) + i
            nums[i], nums[min_index] = nums[min_index], nums[i]
            
            