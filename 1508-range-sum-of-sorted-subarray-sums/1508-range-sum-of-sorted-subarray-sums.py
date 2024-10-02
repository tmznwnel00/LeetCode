class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = []
        
        for i, num1 in enumerate(nums):
            temp = num1
            l.append(temp)
            for num2 in nums[i+1:]:
                temp += num2
                l.append(temp)
        
        l.sort()
        return sum(l[left-1:right]) % (10**9+7)