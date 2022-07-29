class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        #pattern = str(pattern)
        l = len(pattern)
        answer = []
        for i in range(len(words)):
            if len(set(words[i])) == len(set(pattern)):
                d = {}
                #words[i] = str(words[i])
                s = ''
                for j in range(l):
                    if pattern[j] not in d:
                        '''
                        a = list(d.values())
                        if words[i][j] in a:
                            break
                        '''
                        d[pattern[j]] = words[i][j]
                        s += d[pattern[j]]
                    else:
                        s += d[pattern[j]]
                if s == words[i]:
                    answer.append(words[i])
        return answer