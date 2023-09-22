class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            while True:
                if len(t) == 0:
                    return False
                now = t[0]
                t = t[1:]
                if now == c:
                    break
        return True
                    
            