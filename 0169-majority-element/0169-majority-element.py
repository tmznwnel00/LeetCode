class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num = nums[0]
        max_cnt = 0
        
        for num in nums:
            if num == max_num:
                max_cnt += 1
            else:
                max_cnt -= 1
                if max_cnt == 0:
                    max_num = num
                    max_cnt = 1
        return max_num