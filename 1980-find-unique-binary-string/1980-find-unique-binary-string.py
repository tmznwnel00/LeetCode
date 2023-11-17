class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp = 0
        nums.sort()
        answer = -1
        for num in nums:
            if int(num, 2) != temp:
                break
            else:
                temp += 1
        answer = bin(temp)[2:]
        while len(answer) < len(nums[0]):
            answer = '0' + answer
        return answer