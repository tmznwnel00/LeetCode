class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split(' ')
        word_set = set([])
        d = {}
        if len(pattern) != len(s_split):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if s_split[i] in word_set:
                    return False
                d[pattern[i]] = s_split[i]
                word_set.add(s_split[i])
            elif s_split[i] != d[pattern[i]]:
                return False
        return True