from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        answer = 0
        r = dict(Counter(str(ransomNote)))
        m = dict(Counter(str(magazine)))
        k = r.keys()
        for i in range(len(r)):
            if k[i] not in m:
                answer = False
                break
            elif r[k[i]] > m[k[i]]:
                answer = False
                break
            answer = True
        return answer