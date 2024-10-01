class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = []
        
        cnt = 0
        for a in arr:
            if a%k == 0:
                cnt += 1
            else:
                remainder.append(a%k)
            
        if cnt % 2 != 0:
            return False
        
        remainder.sort()
        
        left, right = 0, len(remainder)-1
        
        while left <= right:
            if (remainder[left] + remainder[right]) % k != 0:
                return False
            else:
                left += 1
                right -= 1
        
        
        return True
            