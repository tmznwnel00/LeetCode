class Solution:
    def tribonacci(self, n: int) -> int:
        l = []
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        for i in range(n):
            if i == 0:
                l.append(0)
            elif i == 1:
                l.append(1)
            elif i == 2:
                l.append(1)
            else:
                l.append(l[i - 1] + l[i - 2] + l[i - 3])
        return l[n - 1] + l[n - 2] + l[n - 3]