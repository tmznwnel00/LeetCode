from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        answer = []
        c = dict(Counter(p))
        d = dict(Counter(s[:length]))
        if c == d:
            answer.append(0)
        for i in range(1, len(s) - length + 1):
            d[s[i - 1]] -= 1
            if d[s[i - 1]] == 0:
                del d[s[i - 1]]
            if s[i + length - 1] in d:
                d[s[i + length - 1]] += 1
            else:
                d[s[i + length - 1]] = 1
            if d == c:
                answer.append(i)
        return answer