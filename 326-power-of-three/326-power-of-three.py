class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 1:
            if n == 1:
                return True
            if n % 3 == 0:
                n /= 3
            else:
                return False
            