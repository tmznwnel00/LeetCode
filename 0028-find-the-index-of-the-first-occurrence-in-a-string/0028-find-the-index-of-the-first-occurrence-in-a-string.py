class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            st = haystack[:len(needle)]
            if st == needle:
                return 0
            for h in range(len(needle), len(haystack)):
                st = st[1:] + haystack[h]
                if st == needle:
                    return h - len(needle) + 1