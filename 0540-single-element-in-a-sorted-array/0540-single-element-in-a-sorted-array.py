class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        point = (end - start) // 2
        if len(nums) == 1:
            return nums[0]
        while True:
            if point % 2 == 0:
                if nums[point] == nums[point + 1]:
                    start = point
                elif nums[point] == nums[point - 1]:
                    end = point
                else:
                    return nums[point]
            else:
                if nums[point] == nums[point + 1]:
                    end = point - 1
                elif nums[point] == nums[point - 1]:
                    start = point + 1
                else:
                    return nums[point]
            
            if start == end:
                return nums[start]
            point = (end + start) // 2
            