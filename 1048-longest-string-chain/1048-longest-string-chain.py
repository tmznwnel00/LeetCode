class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [0 for i in range(len(words))]
        words = sorted(words, key = lambda x: len(x), reverse = True)
        d = dict()
        for i, word in enumerate(words):
            if word not in d:
                d[word] = 1
            for j in range(len(word)):
                delete_word = word[:j] + word[j + 1:]
                if delete_word == '' or delete_word not in words:
                    continue
                elif delete_word not in d:
                    d[delete_word] = d[word] + 1
                else:
                    d[delete_word] = max(d[delete_word], d[word] + 1)
        return max(d.values())
                    