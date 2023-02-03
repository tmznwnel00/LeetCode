class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex = {}
        for index, l in enumerate(order):
            lex[l] = index
        for i in range(len(words) - 1):
            for x, y in zip(words[i], words[i + 1]):
                flag = 0
                if lex[x] > lex[y]:
                    return False
                elif lex[x] < lex[y]:
                    break
                else:
                    flag = 1
                    continue
            if flag == 1 and len(words[i]) > len(words[i + 1]):
                return False
        return True