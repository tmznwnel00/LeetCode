class WordDictionary:

    def __init__(self):
        self.s = set([])

    def addWord(self, word: str) -> None:
        self.s.add(word)

    def search(self, word: str) -> bool:
        if '.' in word:
            len_word = len(word)
            for string in self.s:
                if len(string) != len_word:
                    continue
                    
                check = 0
                for index, w in enumerate(word):
                    if w == '.':
                        continue
                    else:
                        if w != string[index]:
                            check = 1
                if check == 0:
                    return True
            return False
        else:
            if word in self.s:
                return True
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)