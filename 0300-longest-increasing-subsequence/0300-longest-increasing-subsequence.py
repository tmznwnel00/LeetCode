class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [[nums[0], 1]]
        
        answer = 0
        for i, num in enumerate(nums):
            if i == 0:
                continue
            l = 0
            r = len(lis)
            while l < r:
                m = (l + r) // 2
                if num > lis[m][0]:
                    l = m + 1
                else:
                    r = m
            
            if l - 1 >= 0:
                lis.insert(l, [num, max(list(map(lambda x:x[1], lis[:l])), default = 0) + 1])
            else:
                lis.insert(l, [num, 1])

        return max(lis, key = lambda x:x[1])[1]