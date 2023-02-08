class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        i = 0
        k = 0
        for j in range(n * 2):
            if k % 2 == 0:
                answer.append(nums[i])
                k += 1
            else:
                answer.append(nums[i + n])
                i += 1
                k += 1
        return answer