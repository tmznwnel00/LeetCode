class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c_set = set([])
        answer = 0
        for i, c in enumerate(s):
            if c in c_set:
                continue
            else:
                for j, c2 in enumerate(s[i+1:][::-1]):
                    if c2 == c:
                        cnt = len(set(s[i+1:][::-1][j+1:]))
                        answer += cnt
                        break
            c_set.add(c)
        
        return answer
                