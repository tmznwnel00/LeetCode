class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        # if left == right:
        #     if nums[left] == target:
        #         return left
        #     else:
        #         return -1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1