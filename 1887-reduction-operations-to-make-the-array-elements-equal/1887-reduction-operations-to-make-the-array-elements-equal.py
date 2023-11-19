class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        temp = 0
        min_val = nums[0]
        for num in nums:
            if num > min_val:
                temp += 1
                min_val = num
            answer += temp 
        return answer