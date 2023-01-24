class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = {i : 0 for i in range(1, n + 1)}
        for i, j in trust:
            if i in l:
                l[i] = -1
            l[j] += 1
        k = 0
        s = []
        for i, j in l.items():
            if j == n - 1:
                s.append(i)
        if len(s) == 1:
            return s[0]
        print(l)
        return -1
            