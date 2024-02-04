class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) // 3):
            if nums[3*i+2] - nums[3*i] > k:
                return None
            answer.append(nums[3*i:3*i+3])

        return answer