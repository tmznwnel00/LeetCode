class Solution(object):
    def isUgly(self, n):
        while True:
            if n == 1 or n == 0:
                break
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                break
        if n == 1:
            return True
        else:
            return False
