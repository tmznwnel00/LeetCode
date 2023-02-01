class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m1 = ''
        m2 = ''
        if len(str1) >= len(str2):
            m1 = str2
            m2 = str1
        else:
            m1 = str1
            m2 = str2
        res = [m1[i: j] for i in range(len(m1))
          for j in range(i + 1, len(m1) + 1)]
        res = sorted(res, key = len, reverse = True)
        l1 = len(m1)
        l2 = len(m2)
        for i in res:
            length = len(i)
            if l1 % length == 0 and l2 % length == 0:
                if i * (l1 // length) == m1 and i * (l2 // length) == m2:
                    return i
            else:
                continue
        return ''