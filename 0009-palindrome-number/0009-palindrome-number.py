class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)
        length = len(s_x)
        left = 0
        right = length - 1
        
        while left < right:
            if s_x[left] != s_x[right]:
                return False
            left += 1
            right -= 1
        return True