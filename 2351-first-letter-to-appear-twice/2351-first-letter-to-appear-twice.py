class Solution(object):
    def repeatedCharacter(self, s):
        d = set()
        for i in range(len(s)):
            if s[i] not in d:
                d.add(s[i])
            else:
                return s[i]
                