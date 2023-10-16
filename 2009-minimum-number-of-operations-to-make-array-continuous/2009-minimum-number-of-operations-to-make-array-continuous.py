class Solution:
    def minOperations(self, nums: List[int]) -> int:
        original_size = len(nums)
        nums = list(set(nums))
        nums.sort()
        
        
        def bs(l, target, num_array):
            index = l
            r = len(num_array) - 1
            while l <= r:
                m = (l+r) //2
                if num_array[m] == target:
                    break
                elif num_array[m] > target:
                    r = m - 1
                elif num_array[m] < target:
                    l = m + 1
            return (l+r) //2
        record = []        
        
        size = len(nums)
        
        for i, num in enumerate(nums):
            temp = bs(i, nums[i] + original_size - 1,  nums)
            
            record.append(original_size - temp + i - 1)
            
        return min(record)