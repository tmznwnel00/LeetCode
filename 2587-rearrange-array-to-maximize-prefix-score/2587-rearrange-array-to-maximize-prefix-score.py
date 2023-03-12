class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        answer = 0
        prefix = []
        now = 0
        for num in nums:
            now += num
            if now > 0:
                answer += 1
        return answer