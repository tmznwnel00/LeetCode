class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = False
        one, two = 0, 0
        answer = 0
        for i, num in enumerate(nums):
            if num == 0:
                answer = max(answer, one + two)
                one, two = two, 0
                flag = True
            else:
                two += 1
        
        answer = max(answer, one + two)

        if not flag:
            answer -= 1

        return answer
                

