from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        l = []
        for i in range(len(strs)):
            l.append(Counter(str(strs[i])))
        d = {}
        for i in range(len(strs)):
            if tuple(sorted(l[i].elements())) in d:
                d[tuple(sorted(l[i].elements()))].append(strs[i])
            else:
                d[tuple(sorted(l[i].elements()))] = [strs[i]]
        return list(d.values())
        
        