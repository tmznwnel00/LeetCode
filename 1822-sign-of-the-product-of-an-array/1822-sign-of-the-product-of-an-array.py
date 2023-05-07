import numpy as np
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        
        temp = 0
        for num in nums:
            if num < 0:
                temp += 1
        
        if temp % 2 == 1:
            return -1
        else:
            return 1
        
        