class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pointer = len(nums) // 2
        check = -1
        while True:
            # print(pointer, check)
            if pointer == -1:
                return 0
            if pointer == len(nums):
                return len(nums)
            if nums[pointer] == target:
                return pointer
            elif (check == 1 or check == -1) and nums[pointer] < target:
                pointer += 1
                check = 1
            elif check == 0 and nums[pointer] < target:
                return pointer + 1
            elif (check == 0 or check == -1) and nums[pointer] > target:
                pointer -= 1
                check = -1
            else:
                return pointer
                